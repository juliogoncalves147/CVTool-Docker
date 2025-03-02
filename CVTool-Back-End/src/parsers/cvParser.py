from lark.visitors import Interpreter
from lark import Lark, Tree

gramatica = r'''//
//Regras Sintaticas
//
start: document

document: (command | element | LB document RB)*

element: /[^\{\}\n\\]+/ 

command: "\\" /[a-zA-Z\.\^\%úáíóãé'0-9\-çã\'\\\,\#\+\`\(\)\@\&\:\/\~\?\ÿ\;õêàô\ª\º]+/ (( LB (document)* RB )*)

LB: "{"

RB: "}"

//Tratamento dos espaços em branco
%import common.WS
%ignore WS
'''

class CVParser:
    def __init__(self):
        self.result = []
        self.nivel = 0

    def parse(self, text):
        parser = Lark(gramatica)
        tree = parser.parse(text)
        valor = MyInterpreter().visit(tree)  # Pass the CVParser instance to MyInterpreter
        return valor
    

class MyInterpreter(Interpreter):
    # Auxiliar Method
    def modify_dicts_by_idsSection(self, id_list, key_to_modify, new_value):
        for item in self.result:
            if int(item[key_to_modify]) in id_list:
                item["section"] = new_value
    
    def modify_dicts_by_idsSubSection(self, id_list, key_to_modify, new_value):
        for item in self.result:
            if int(item[key_to_modify]) in id_list:
                item["subsection"] = new_value

    # Interpreter Methods
    def __init__(self):
        self.nivel = 0
        self.result = []
        self.sectionAtual = ''
        self.subSectionAtual = ''
        self.newSection = False
        self.newSubSection = False
        self.id = 1
        self.reserved = False
        self.cacheIdsSections = []
        self.cacheIdsSubSections = []
        
        
    def start(self, tree):
        self.visit_children(tree)
        return self.result
        
    def document(self, tree):
        for elemento in tree.children:
            if(type(elemento) == Tree):
                t = self.visit(elemento)
                #print("T1 " + elemento.data + " " + str(t) + "\n")
                if(elemento.data == "element" and self.newSection):
                    self.sectionAtual = str(t)
                    valor = {
                        "id": str(self.id),
                        "tipo": elemento.data.value,
                        "valor": str(t),
                        "nivel": self.nivel,
                        "section": self.sectionAtual,
                        "subsection": self.subSectionAtual,
                        "reserved": self.reserved
                    }
                    self.result.append(valor)
                    self.newSection = False
                    self.newSubSection = False
                    self.id += 1
                    self.modify_dicts_by_idsSection(self.cacheIdsSections, "id",  self.sectionAtual)
                    self.cacheIdsSections = []
                elif(elemento.data == "element" and self.newSubSection):
                    self.subSectionAtual = str(t)
                    valor = {
                        "id": str(self.id),
                        "tipo": elemento.data.value,
                        "valor": str(t),
                        "nivel": self.nivel,
                        "section": self.sectionAtual,
                        "subsection": self.subSectionAtual,
                        "reserved": self.reserved
                    }
                    self.result.append(valor)
                    self.newSubSection = False
                    self.id += 1
                    self.modify_dicts_by_idsSubSection(self.cacheIdsSubSections, "id",  self.subSectionAtual)
                    self.cacheIdsSubSections = []
                elif(elemento.data == "element"):
                    valor = {
                        "id": str(self.id),
                        "tipo": elemento.data.value,
                        "valor": str(t),
                        "nivel": self.nivel,
                        "section": self.sectionAtual,
                        "subsection": self.subSectionAtual,
                        "reserved": self.reserved
                    }
                    self.result.append(valor)
                    self.id += 1
                elif(elemento.data == "command" and (str(t) == "begin" or str(t) == "end" or str(t) == "url" or str(t) == "href")):
                    self.reserved = True
                    valor = {
                        "id": str(self.id),
                        "tipo": elemento.data.value,
                        "valor": str(t),
                        "nivel": self.nivel,
                        "section": self.sectionAtual,
                        "subsection": self.subSectionAtual
                    }
                    self.result.append(valor)
                    self.id += 1
                elif(elemento.data == "command" and str(t) == "section"):
                    self.sectionAtual = ''
                    self.subSectionAtual = ''
                    valor = {
                        "id": str(self.id),
                        "tipo": elemento.data.value,
                        "valor": str(t),
                        "nivel": self.nivel,
                        "section": self.sectionAtual,
                        "subsection": self.subSectionAtual
                    }
                    self.result.append(valor)
                    self.newSection = True
                    self.cacheIdsSections.append(self.id)
                    self.id += 1
                elif(elemento.data == "command" and str(t) == "subsection"):
                    self.subSectionAtual = ''
                    valor = {
                        "id": str(self.id),
                        "tipo": elemento.data.value,
                        "valor": str(t),
                        "nivel": self.nivel,
                        "section": self.sectionAtual,
                        "subsection": self.subSectionAtual
                    }
                    self.result.append(valor)
                    self.newSubSection = True
                    self.cacheIdsSubSections.append(self.id)
                    self.id += 1
                elif(elemento.data == "command"):
                    valor = {
                        "id": str(self.id),
                        "tipo": elemento.data.value,
                        "valor": str(t),
                        "nivel": self.nivel,
                        "section": self.sectionAtual,
                        "subsection": self.subSectionAtual
                    }
                    self.result.append(valor)
                    self.id += 1
            else:
                if (elemento.type=='LB'):
                    #print("T1 " + " Left Bracket " + "{" + "\n")
                    self.nivel += 1
                    valor = {
                        "id": str(self.id),
                        "tipo": "LB",
                        "valor": "{",
                        "nivel": self.nivel,
                        "section": self.sectionAtual,
                        "subsection": self.subSectionAtual
                    }
                    self.result.append(valor)
                    if self.newSection:
                        self.cacheIdsSections.append(self.id)
                    if self.newSubSection:
                        self.cacheIdsSubSections.append(self.id)
                    self.id += 1
                elif (elemento.type=='RB'):
                    #print("T1 " + " Right Bracket " + "}" + "\n")
                    self.nivel -= 1
                    valor = {
                        "id": str(self.id),
                        "tipo": "RB",
                        "valor": "}",
                        "nivel": self.nivel,
                        "section": self.sectionAtual,
                        "subsection": self.subSectionAtual
                    }
                    if self.reserved:
                        self.reserved = False
                    self.result.append(valor)
                    self.id += 1
                elif (elemento.type=='PERC'):
                    valor = {
                        "id": str(self.id),
                        "tipo": "PERC",
                        "valor": "%",
                        "nivel": self.nivel,
                        "section": self.sectionAtual,
                        "subsection": self.subSectionAtual
                    }
                    self.result.append(valor)
                    self.id += 1
                
                
    def element(self, tree):
        for elemento in tree.children:
            if(type(elemento) == Tree):
                t = self.visit(elemento)
                #print("T2: " + elemento + " " + str(t))
            else:
                return elemento
            
    
    def command(self, tree):
        for elemento in tree.children:
            if(type(elemento) == Tree):
                t = self.visit(elemento)
                #print("T3: " + elemento + " " + str(t))
            else:
                return elemento