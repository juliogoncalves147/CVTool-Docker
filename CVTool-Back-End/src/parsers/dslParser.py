# cv_parser.py
import json
import pprint
import re
from lark.visitors import Interpreter
from lark import Lark, Tree, Visitor, v_args


gramatica = r'''//
//Regras Sintaticas
//
start: query

query: selectquery | translatequery | export_query | reorder_query

selectquery: "SELECT" sectionlist whereclause?

whereclause: "WHERE" condition

translatequery: "TRANSLATE" "FROM" source "TO" output

export_query: "EXPORT" "TO" output 

reorder_query: "REORDER" section ("," section)*

sectionlist: ALL | section (VIRG section)*

section:  NAME 

condition: andcondition  ("OR" andcondition)*

andcondition: "(" condition ")" | simplecondition ("AND" simplecondition)*

simplecondition: SECTION sectionoperator value | DATE dateoperator value | THEME sectionoperator value

dateoperator: EQUALS | DIFFER | GREATER | MINOR | GREQ | MIEQ

sectionoperator: EQUALS | DIFFER

value: /\'(.*?)\'/

source: NAME

output: NAME

NAME: /\'(.*?)\'/

GREATER: ">"

GREQ: ">="

MIEQ: "<="

EQUALS: "="

DIFFER: "!="

MINOR: "<"

ALL: "*"

VIRG: /\,/

SECTION: "SECTION"

DATE: "DATE"

THEME: "THEME"


//Tratamento dos espaços em branco
%import common.WS
%ignore WS
'''

class DSLParser:
    def __init__(self):
        self.result = []

    def parse(self, text):
        parser = Lark(gramatica)
        tree = parser.parse(text)
        valor = MyInterpreter().visit(tree)  # Pass the CVParser instance to MyInterpreter
        return valor
    

class MyInterpreter(Interpreter):
    # Auxiliar Method
    # Interpreter Methods
    def __init__(self):
        self.result = []
        self.filters = []
        self.translations = []
        
    def start(self, tree):
        return self.visit_children(tree)
    
    def query(self, tree):
        for elemento in tree.children:
            return self.visit(elemento)
                
    def selectquery(self, tree):
        print(" -- Select Query --")
        query = {}
        query["queryField"] = "SELECT"
        query["clauses"] = ""
        for elemento in tree.children:
            if(type(elemento) == Tree):
                t = self.visit(elemento)
                if elemento.data == "sectionlist":
                    query["sectionlist"] = t
                    #print("Section List: " + str(t))
                elif elemento.data == "whereclause":
                    #print("Where Clause: " + str(t))
                    query["clauses"] = t
        return query
        
    
    def whereclause(self, tree):
        for elemento in tree.children:
            if(type(elemento) == Tree):
                return self.visit(elemento)
            else:
                return elemento
    
    def translatequery(self, tree):
        print(" -- Translate Query --")
        query = {}
        query["queryField"] = "TRANSLATE"
        for elemento in tree.children:
            if(type(elemento) == Tree):
                if elemento.data == "source":
                    query["source"] = str(self.visit(elemento))
                elif elemento.data == "output":
                    query["output"] = str(self.visit(elemento))
        return query
                
    def export_query(self, tree):
        for elemento in tree.children:
            if(type(elemento) == Tree):
                t = self.visit(elemento)
            else:
                return elemento
    
    def reorder_query(self, tree):
        print(" -- Reorder Query --")
        sectionsList = []
        for elemento in tree.children:
            if(type(elemento) == Tree):
                sectionsList.append(str(self.visit(elemento)))
            else:
                return elemento
        print("Reorder Sections: " + str(sectionsList))
                
    def sectionlist(self, tree):
        t  = []
        for elemento in tree.children:
            if(type(elemento) == Tree):
                t.append(str(self.visit(elemento)))
            else:
                if (elemento.type == "ALL"):
                    t.append("ALL")
        return t
    
    def section(self, tree):
        for elemento in tree.children:
            if(type(elemento) == Tree):
                return self.visit(elemento)
            else:
                if elemento.type == "NAME":
                    match = re.match(r"'(.*?)'", elemento.value)
                    if match:
                        return match.group(1)
                
    def condition(self, tree):
        t = []
        for elemento in tree.children:
            if(type(elemento) == Tree):
                t.extend(self.visit(elemento))
            else:
                t.extend(elemento)
        return t
                
    def andcondition(self, tree):
        t = []
        for elemento in tree.children:
            if(type(elemento) == Tree):
                t.append(self.visit(elemento))
            else:
                t.append(elemento)
        return t
                
    def simplecondition(self, tree):
        clause = {}
        for elemento in tree.children:
            if(type(elemento) == Tree):
                if elemento.data == "sectionoperator" or elemento.data == "dateoperator":
                    clause["operator"] = str(self.visit(elemento))
                elif elemento.data == "value":
                    clause["value"] = str(self.visit(elemento))
                elif elemento.data == "section":
                    clause["section"] = str(self.visit(elemento))
            else:
                clause["field"] = str(elemento)
        return clause
                
    def sectionoperator(self, tree):
        for elemento in tree.children:
            if(type(elemento) == Tree):
                return self.visit(elemento)
            else:
                return elemento
            
    def dateoperator(self, tree):
        for elemento in tree.children:
            if(type(elemento) == Tree):
                return self.visit(elemento)
            else:
                return elemento
                
    def value(self, tree):
        for elemento in tree.children:
            if(type(elemento) == Tree):
                t = self.visit(elemento)
            else:
                match = re.match(r"'(.*?)'", elemento.value)
                if match:
                    return match.group(1)
                
    def year(self, tree):
        for elemento in tree.children:
            if(type(elemento) == Tree):
                t = self.visit(elemento)
            else:
                return elemento
                
    def source(self, tree):
        for elemento in tree.children:
            if(type(elemento) == Tree):
                t = self.visit(elemento)
            else:
                if elemento.type == "NAME":
                    match = re.match(r"'(.*?)'", elemento.value)
                    if match:
                        return match.group(1)
                
    def output(self, tree):
        for elemento in tree.children:
            if(type(elemento) == Tree):
                t = self.visit(elemento)
            else:
                if elemento.type == "NAME":
                    match = re.match(r"'(.*?)'", elemento.value)
                    if match:
                        return match.group(1)
    

#cv_parser = DSLParser()
#parsed_file = cv_parser.parse("SELECT * WHERE (SECTION = 'Education Universitary' AND DATE > '2010') OR (SECTION = 'Professional Experience' AND DATE = '2010')")
#print(parsed_file)
#print(parsed_file)
#print("Filters:")
#print(parsed_file.filters)
#print("\nTranslations:")
#print(parsed_file.translations)