from .CommonsHelper import sortByIndexAsc


def checkToEndCommands(parsedData):
    toEndCommands = []
    beginCommand = False
    for item in parsedData:
        if (item.get("tipo") == "command" and item.get("valor") == "begin" and item.get("section") == ""):
            beginCommand = True
        if (beginCommand and item.get("tipo") == "element"):
            toEndCommands.append(item)
            beginCommand = False

    return toEndCommands

def addEndCommands(item, indice):
    lista = [{'id': str(9999+indice+1), 'tipo': 'command', 'valor': 'end', 'nivel': 0, 'section': ''},
            {'id': str(9999+indice+2), 'tipo': 'LB', 'valor': '{', 'nivel': 0, 'section': ''}]
    newItem = item.copy()
    newItem['id'] = str(9999+indice+3)
    lista.append(newItem)
    lista.append({'id': str(9999+indice+4), 'tipo': 'RB', 'valor': '}', 'nivel': 0, 'section': ''})
    return lista

def getSection(parsedData, sectionName):
    lista = []
    for item in parsedData:
        if(item.get("section") == sectionName):
            lista.append(item)
    return lista

def deleteSection(parsedData, startId, endId):
    result = []
    for item in parsedData:
        item_id = int(item.get("id"))
        if not (startId <= item_id <= endId):
            result.append(item)
        else:
            print(f"Removing item with id: {item_id}")
    return result


def addSection(parsedData, parsedSection):
    parsedData.extend(parsedSection)
    return sortByIndexAsc(parsedData)

def getWithoutSection(parsedData, sectionName):
    lista = []
    for item in parsedData:
        if(item.get("section") != sectionName):
            lista.append(item)
    return lista

def filterSection(parsedData, section_names):
    lista = []
    toEndCommands = checkToEndCommands(parsedData)
    toEndCommands.reverse()
    for item in parsedData:
        if item.get("section") == "" or item.get("section") in section_names:
            lista.append(item) 
    
    indice = 1
    for item in toEndCommands:
        itens = addEndCommands(item, indice)
        indice += 5
        lista.extend(itens)
    
    sortedData = sortByIndexAsc(lista)
    return sortedData

        
def filterSectionQuery(parsedData, sectionsListNames):
    return filterSection(parsedData, sectionsListNames)