
# Importing necessary libraries
import logging
from lark import UnexpectedCharacters

from src.parsers.cvParser import CVParser
from src.parsers.dslParser import DSLParser
from src.filters.filterDate import filterDateQuery
from src.filters.filterTheme import filterThemeQuery
from src.filters.filterSection import filterSectionQuery, getSection, deleteSection, addSection, getWithoutSection, getSubSection , getWithoutSubSection, reorderSectionsQuery, dropSectionsQuery
from src.filters.translate import translateQuery
from src.writer import Writer

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def printRunTime(start_time, end_time):
    elapsed_time = end_time - start_time
    minutes = int(elapsed_time // 60)
    seconds = elapsed_time % 60
    print(f"Elapsed time:  " + str(minutes) + "  minutes and " +  str(seconds) + " seconds")  

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

class Controller:
    def __init__(self):
        self.cv_parser = CVParser()
        self.dsl_parser = DSLParser()
        self.filtered_file = None
        
    def handle_query(self, fileName, query):
        logger.info(f"Processing file: {fileName} with query: {query}")
        file_path = f"{fileName}"
        
        text = self.__readFile(file_path)

        parsed_file = self.__parseFile(text)

        parsedDSL = self.__parseQuery(query)

        self.__processFile(file_path, parsed_file, parsedDSL)

        logger.info(f"Query processed successfully: {query}")
        
        return file_path
    
    def treat_query(self, parsedDSL, parsed_file):
        # Process each command in the query
        for item in parsedDSL:
            if (self.__isShow(item)):
                file = self.__processShowCommand(parsed_file, item)

            elif (self.__isTranslate(item)):
                file = self.__processTranslateCommand(parsed_file, item)

            elif (self.__isReorder(item)):
                file = self.__processReorderCommand(parsed_file, item)
                
            elif (self.__isDrop(item)):
                file = self.__processDropCommand(parsed_file, item)


        Writer.writeStructuredData(parsed_file, "run_logs/Filtered_Data_Struct.txt") 

        return file

    def __readFile(self, file_path):
        try:
            with open(file_path, 'r') as file:
                text = file.read()
        except Exception as e:
            logger.error(f"Error reading file:  {file_path} - {e}")
            raise Exception
        return text
    
    def __parseFile(self, text):
        try:
            parsed_file = self.cv_parser.parse(text)
        except Exception as e:
            logger.error(f"Error parsing file content: {e}")
            raise Exception
        return parsed_file
    
    def __parseQuery(self, query):
        try:
            parsedDSL = self.dsl_parser.parse(query)
            logger.debug(f"Parsed DSL: {parsedDSL}")
        except UnexpectedCharacters as e:
            logger.error(f"Invalid DSL query: {query} - {e}")
            raise Exception
        except Exception as e:
            logger.error(f"Unexpected error while parsing DSL query: {query} - {e}")
            raise Exception
        return parsedDSL
    
    def __processFile(self, file_path, parsed_file, parsedDSL):
        try:
            self.filtered_file = self.treat_query(parsedDSL, parsed_file)
            Writer.structToFile(self.filtered_file, file_path)
        except KeyError as e:
            logger.error(f"Processing file error: {e}")
            raise Exception
        except Exception as e:
            logger.error(f"Unexpected error during query processing: {e}")
            raise Exception
    
    def __processReorderCommand(self, parsed_file, item):
        # Process Reorder Query
        sectionlist = item.get("sectionlist")

        file = None
        file = reorderSectionsQuery(parsed_file, sectionlist)

        if file == None:
            print("Query Error 1: Section doesn't exist.")
            return KeyError
        
        return file
    
    def __processDropCommand(self, parsed_file, item):
    # Check for the presence of 'sectionlist' or 'subsectionlist' in the dictionary
        #print("Processing Drop Command")
        sectionlist = item.get("sectionlist")
        #print("Section List: " + str(sectionlist))
    # Initialize file as None
        file = None
        file = dropSectionsQuery(parsed_file, sectionlist)

        #print("File: " + str(len(file)))
    # Handle case where section or subsection doesn't exist
        if file is None:
            print("Query Error: Specified section or subsection doesn't exist.")
            return KeyError

        return file
    
    def __processTranslateCommand(self, parsed_file, item):
        # Process Translate Query
        return translateQuery(parsed_file, item.get("source"), item.get("output"))

    def __processShowCommand(self, parsed_file, item):
        # Process Show Query
        sectionlist = item.get("sectionlist")
        logger.info("processShowCommand: Section List: " + str(sectionlist))
        
        file = None
        # Get all sections
        if len(sectionlist) == 1 and sectionlist[0] == "ALL":
            file = parsed_file
        else: # Get specific sections
            self.__checkSectionQuery(sectionlist, item.get("clauses"))
            file = filterSectionQuery(parsed_file, sectionlist)

        if file == None:
            logger.error("processShowCommand: Specified sections doesn't exist.")
            return KeyError
        
        group = item.get("clauses")
        # Simple Command
        if not is_list_of_list_of_dicts(group):
            file = self.__processClauses(file, group)
        else: # Complex Command
            for groupclauses in group:
                file = self.__processClauses(file, groupclauses)
        
        return file

    def __isShow(self, item):
        # Check if the query is a SHOW command
        return item.get("queryField").lower() == "SHOW".lower()
    
    def __isSectionFilter(self, clause):
        # Check if the query is a SECTION command
        return clause.get("field").lower() == "SECTION".lower()
    
    def __isSubSectionFilter(self, clause):
        return clause.get("field").lower() == "SUBSECTION".lower()
    
    def __isDateFilter(self, clause):
        return clause.get("field").lower() == "DATE".lower()
    
    def __isThemeFilter(self, clause):
        return clause.get("field").lower() == "THEME".lower()

    def __isReorder(self, item):
        # Check if the query is a REORDER command
        return item.get("queryField").lower() == "REORDER".lower()

    def __isDrop(self, item):
        # Check if the query is a DROP command
        return item.get("queryField").lower() == "DROP".lower()

    def __isTranslate(self, item):
        # Check if the query is a TRANSLATE command
        return item.get("queryField").lower() == "TRANSLATE".lower()
    
    def __processClauses(self, file, group):
        # Process the filters from the show query
        logger.info("Processing Group Clauses:" + str(group))

        section = file
        subsection = file
        sectionDifferent = False
        subsectionDifferent = False
        keepSection = None
        keepSubSection = None
        isSubSection = False

        for clause in group:
            if self.__isSectionFilter(clause): 
                if clause.get("operator") == "=":
                    section = getSection(file, clause.get("value"))

                    if (section == None or len(section) == 0):
                        raise KeyError("Query Error 2.1: Section doesn't exist.")
                    
                elif clause.get("operator") == "!=":
                    sectionDifferent = True

                    keepSection = getSection(file, clause.get("value"))

                    section = getWithoutSection(file, clause.get("value"))

                    if (keepSection == None or len(keepSection) == 0):
                        raise KeyError("Query Error 2.1: Section doesn't exist.")

            elif self.__isSubSectionFilter(clause):
                isSubSection = True

                if clause.get("operator") == "=":
                    subsection = getSubSection(file, clause.get("value"))

                    if (subsection == None or len(subsection) == 0):
                        raise KeyError("Query Error 2.2: SubSection doesn't exist.")
                    
                elif clause.get("operator") == "!=":
                    subsectionDifferent = True

                    keepSubSection = getSubSection(file, clause.get("value"))

                    subsection = getWithoutSubSection(file, clause.get("value"))

                    if (keepSubSection == None or len(keepSubSection) == 0):
                        raise KeyError("Query Error 2.2: SubSection doesn't exist.")

            elif self.__isDateFilter(clause):

                if isSubSection:
                    startId = int(subsection[0].get("id"))
                    endId = int(subsection[-1].get("id"))

                    subsection = filterDateQuery(subsection, clause.get("value"), clause.get("operator"))

                    if subsectionDifferent:
                        file = addSection(subsection, keepSubSection)
                        subsectionDifferent = False
                        keepSubSection = None

                    else:
                        file = deleteSection(file, startId, endId)
                        file = addSection(file, subsection)

                    isSubSection = False

                else:
                    startId = int(section[0].get("id"))
                    endId = int(section[-1].get("id"))

                    section = filterDateQuery(section, clause.get("value"), clause.get("operator"))

                    if sectionDifferent:
                        file = addSection(section, keepSection)
                        sectionDifferent = False
                        keepSection = None

                    else:
                        file = deleteSection(file, startId, endId)
                        file = addSection(file, section)
            elif self.__isThemeFilter(clause):
                if isSubSection:
                    startId = int(subsection[0].get("id"))
                    endId = int(subsection[-1].get("id"))

                    subsection = filterThemeQuery(subsection, clause.get("value"), clause.get("operator"))

                    if subsectionDifferent:
                        file = addSection(subsection, keepSubSection)
                        subsectionDifferent = False
                        keepSubSection = None

                    else:
                        file = deleteSection(file, startId, endId)
                        file = addSection(file, subsection)

                    isSubSection = False

                else:
                    startId = int(section[0].get("id"))
                    endId = int(section[-1].get("id"))

                    section = filterThemeQuery(section, clause.get("value"), clause.get("operator"))

                    if sectionDifferent:
                        file = addSection(section, keepSection)
                        sectionDifferent = False
                        keepSection = None

                    else:
                        file = deleteSection(file, startId, endId)
                        file = addSection(file, section)
        return file
    
    def __checkSectionQuery(self,sectionlist, group):
        # Assert the sections provides for the query exists on the file
        for groupclauses in group:
            logger.info("Check Section Query - Group Clauses: " + str(groupclauses))
            # Check if groupclauses is a list of elements
            if isinstance(groupclauses, list):
                for clause in groupclauses:
                    if clause.get("field").lower() == "SECTION".lower():
                        if clause.get("value") not in sectionlist:
                            logger.error("Section not in list")
                            exit()
            else:
                # If groupclauses is a single element, process it directly
                clause = groupclauses
                if clause.get("field").lower() == "SECTION".lower():
                    if clause.get("value") not in sectionlist:
                        logger.error("Section not in list")
                        exit()