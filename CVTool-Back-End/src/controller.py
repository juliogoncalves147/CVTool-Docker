import pprint
import re
import subprocess
import time
import threading
import queue
import unicodedata
import dateparser
import logging
from lark import UnexpectedCharacters

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
from ratelimit import limits, sleep_and_retry
import spacy
from deep_translator import GoogleTranslator


from .parsers.cvParser import CVParser
from .parsers.dslParser import DSLParser
from .filters.filterDate import filterDateQuery
from .filters.filterSection import filterSectionQuery, getSection, deleteSection, addSection, getWithoutSection
from .filters.translate import translateQuery
from .writer import writer

from concurrent.futures import ThreadPoolExecutor, as_completed
import concurrent.futures

def printRunTime(start_time, end_time):
    elapsed_time = end_time - start_time
    minutes = int(elapsed_time // 60)
    seconds = elapsed_time % 60
    print(f"Elapsed time:  " + str(minutes) + "  minutes and " +  str(seconds) + " seconds")  

def checkSectionQuery(sectionlist, group):
    for groupclauses in group:
        print("Group Clauses: " + str(groupclauses))
    
        # Check if groupclauses is a list of elements
        if isinstance(groupclauses, list):
            for clause in groupclauses:
                if clause.get("field") == "SECTION":
                    if clause.get("value") not in sectionlist:
                        print("Section not in list")
                        print("Section: " + clause.get("value"))
                        print("List: " + str(sectionlist))
                        exit()
        else:
            # If groupclauses is a single element, process it directly
            clause = groupclauses
            if clause.get("field") == "SECTION":
                if clause.get("value") not in sectionlist:
                    print("Section not in list")
                    print("Section: " + clause.get("value"))
                    print("List: " + str(sectionlist))
                    exit()

def is_list_of_list_of_dicts(variable):
    if not isinstance(variable, list):
        return False
    
    for item in variable:
        if not isinstance(item, list):
            return False
        for sub_item in item:
            if not isinstance(sub_item, dict):
                return False
    
    return True


def processClauses(file, group):
    print("Group Clauses:" + str(group))
    section = file
    sectionDifferent = False
    keepSection = None
    for clause in group:
        # Queremos mexer no documento em partes, ou mexer como um todo?
        if clause.get("field") == "SECTION":
            if clause.get("operator") == "=":
                section = getSection(file, clause.get("value"))
                if (section == None or len(section) == 0):
                    #print("Query Error 2: Section doesn't exist.")
                    raise KeyError("Query Error 2.1: Section doesn't exist.")
            elif clause.get("operator") == "!=":
                sectionDifferent = True
                keepSection = getSection(file, clause.get("value"))
                section = getWithoutSection(file, clause.get("value"))
                if (keepSection == None or len(keepSection) == 0):
                    #print("Query Error 2: Section doesn't exist.")
                    raise KeyError("Query Error 2.2: Section doesn't exist.")
        elif clause.get("field") == "DATE":
                startId = int(section[0].get("id"))
                endId = int(section[-1].get("id"))
                print("Start: " + str(startId))
                print("End: " + str(endId))
                section = filterDateQuery(section, clause.get("value"), clause.get("operator"))
                if sectionDifferent:
                    file = addSection(section, keepSection)
                    sectionDifferent = False
                    keepSection = None
                else:
                    file = deleteSection(file, startId, endId)
                    file = addSection(file, section)
    return file

def treat_query(parsedDSL, parsed_file):
    for item in parsedDSL:
        if (item.get("queryField") == "SELECT"):
            
            sectionlist = item.get("sectionlist")
            print(sectionlist)
            
            file = None
            # How to see list size
            if len(sectionlist) == 1 and sectionlist[0] == "ALL":
                print("All Sections")
                file = parsed_file
            else:
                checkSectionQuery(sectionlist, item.get("clauses"))
                file = filterSectionQuery(parsed_file, sectionlist)
                
            if file == None:
                print("Query Error 1: Section doesn't exist.")
                return KeyError
            
            group = item.get("clauses")
            
            if not is_list_of_list_of_dicts(group):
                file = processClauses(file, group)
            else:
                for groupclauses in group:
                    file = processClauses(file, groupclauses)
        elif (item.get("queryField") == "TRANSLATE"):
            file = translateQuery(parsed_file, item.get("source"), item.get("output"))
    return file
# comment multiline

'''
def main():
    # Ficheiro Input
    file = open('/Users/juliogoncalves/Desktop/Mestrado/EL/EG/CVToolProject/BackEnd/docs/prhCV.tex', 'r')
    text = file.read()
    file.close()
    
    # Initialize the CVParser
    cv_parser = CVParser()
    parsed_file = cv_parser.parse(text)
    
    # Write the structured data\
    writer.writeStructuredData(parsed_file, "../generated_docs/Parsed_Data_Struct.txt")   
    # Write the file again, without any modifications in the structure
    writer.structToFile(parsed_file, "../generated_docs/Parsed_File.tex")
    
    # Query
    query = "SELECT * WHERE (SECTION = 'Work experience' AND DATE > '2010') OR (SECTION = 'Education and training' AND DATE >= '2010')"
    #query = "TRANSLATE FROM 'auto' TO 'fr'"
    
    # Initialize the DSLParser
    dsl_parser = DSLParser()
    parsedDSL = dsl_parser.parse(query)
    print("Input Query: " + str(query))
    print("Parsed Query: " + str(parsedDSL))
    
    start_time = time.time()
    try:
        file = handle_query(parsedDSL, parsed_file)                       
    except KeyError as e:
        print(f"Query Error: {e}")
        return e
    except Exception as e:
        print(f"Query Error: Some '()' are missing")
        return e
    
    
    writer.writeStructuredData(file, "../generated_docs/Filtered_Data_Struct.txt")
    writer.structToFile(file, "../generated_docs/Filtered_File.tex")
    
    end_time = time.time()
    
    printRunTime(start_time, end_time)
    
    # -------------- FILTER DATE --------------
    # ParsedData, Ano, Operador
    #filteredData = filterDateQuery(parsed_file, "2019", "maiorIgual")
    
    # -------------- FILTER SECTION --------------
    # Nomes das secções tem que ser texto limpo
    # ParsedData, Lista de Nomes das Secções
    #filteredData = filterSectionQuery(parsed_file, ["Outras atividades consideradas relevantes para a missão do IPB"])
    
    # -------------- TRANSLATE --------------
    # ParsedData, From Language, To Language
    #filteredData = translateQuery(parsedData=parsed_file, from_language="auto", to_language="hr")
    
    #subprocess.run(['latexindent', '-l', '-s', '-w', "FilteredFile.tex"])
    
    #subprocess.run('rm -rf *.bak*', shell=True, capture_output=True, text=True) 
    

#main()

'''

class Controller:
    def __init__(self):
        self.cv_parser = CVParser()
        self.dsl_parser = DSLParser()
        self.filtered_file = None
        
        
    def handle_query(self, fileName, query):
        logger.info(f"Processing file: {fileName} with query: {query}")
        file_path = f"{fileName}"
        
        try:
            with open(file_path, 'r') as file:
                text = file.read()
        except Exception as e:
            print("ERROR")
            logger.error(f"Error reading file:  {file_path} - {e}")
            raise Exception

        try:
            parsed_file = self.cv_parser.parse(text)
        except Exception as e:
            logger.error(f"Error parsing file content: {e}")
            raise Exception

        try:
            parsedDSL = self.dsl_parser.parse(query)
            logger.debug(f"Parsed DSL: {parsedDSL}")
        except UnexpectedCharacters as e:
            logger.error(f"Invalid DSL query: {query} - {e}")
            raise Exception
        except Exception as e:
            logger.error(f"Unexpected error while parsing DSL query: {query} - {e}")
            raise Exception

        try:
            self.filtered_file = treat_query(parsedDSL, parsed_file)
            writer.structToFile(self.filtered_file, file_path)
        except KeyError as e:
            logger.error(f"Query processing error: {e}")
            raise Exception
        except Exception as e:
            logger.error(f"Unexpected error during query processing: {e}")
            raise Exception

        logger.info(f"Query processed successfully: {query}")
        return file_path