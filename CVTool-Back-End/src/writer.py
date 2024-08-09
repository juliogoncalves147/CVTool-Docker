

class writer:
    def __init__(self):
        pass
    
    def writeStructuredData(parsedFile, path):
        with open(path, "w") as f:
            for item in parsedFile:
                f.write(str(item) + ",\n")
    
    def structToFile(lista, path):
        try:
            with open(path, 'w') as f:
                for index, item in enumerate(lista):
                    try:
                        print(f"Processing item {index}: {item}")
    
                        if item.get("tipo") == "command" and item.get("valor").strip() == "%":
                            f.write("\\" + item.get("valor") + "\n")
                            print(f"Wrote command with %: \\" + item.get("valor"))
    
                        elif item.get("tipo") == "command" and item.get("valor") == "\\":
                            # Add the \n before to avoid cases of %----------------\\command
                            f.write(" " + item.get("valor") + item.get("valor") + "\n")
                            print(f"Wrote command with backslash: " + item.get("valor"))
    
                        elif item.get("tipo") == "command":
                            f.write("\n" + "\\" + item.get("valor"))
                            print(f"Wrote general command: \\" + item.get("valor"))
    
                        if item.get("tipo") == "element" and item.get("valor") is not None:
                            if item.get("reserved") == True or item.get("section") == '':
                                f.write(item.get("valor"))
                                print(f"Wrote reserved or sectionless element: {item.get('valor')}")
                            else:
                                f.write(item.get("valor"))
                                print(f"Wrote element: {item.get('valor')}")
    
                        elif item.get("tipo") == "element":
                            f.write(item.get("valor"))
                            print(f"Wrote element: {item.get('valor')}")
    
                        if item.get("tipo") == "LB" and item.get("valor") == "{":
                            f.write("{")
                            print(f"Wrote LB: {item.get('valor')}")
    
                        elif item.get("tipo") == "RB" and item.get("valor") == "}":
                            f.write("}")
                            print(f"Wrote RB: {item.get('valor')}")
                    except Exception as e:
                        print(f"Error processing item {index}: {e}, item: {item}")
    
        except Exception as e:
            print(f"Failed to open or write to file at {path}: {e}")
