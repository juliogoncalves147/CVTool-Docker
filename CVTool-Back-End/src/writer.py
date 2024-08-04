

class writer:
    def __init__(self):
        pass
    
    def writeStructuredData(parsedFile, path):
        with open(path, "w") as f:
            for item in parsedFile:
                f.write(str(item) + ",\n")
    
    def structToFile(lista, path):
        with open(path, 'w') as f:
            for item in lista:
                if(item.get("tipo") == "command" and item.get("valor").strip() == "%"):
                    f.write("\\" + item.get("valor") + "\n")
                elif(item.get("tipo") == "command" and item.get("valor") == "\\"):
                    # Add the \n before to avpod cases of %----------------\\command
                    f.write(" " + item.get("valor") + item.get("valor") + "\n")
                elif(item.get("tipo") == "command"):                    #f.write("\n" + "\\" + item.get("valor"))
                    f.write("\n" + "\\" + item.get("valor") + "")
                
                if(item.get("tipo") == "element" and item.get("valor") != None):
                    if(item.get("reserved") == True or item.get("section") == ''):
                        f.write(item.get("valor"))
                    else:
                        f.write(item.get("valor"))
                elif(item.get("tipo") == "element"):
                    f.write(item.get("valor"))
                
                if(item.get("tipo") == "LB" and item.get("valor") == "{"):
                    f.write("{")
                elif(item.get("tipo") == "RB" and item.get("valor") == "}"):
                    f.write("}")