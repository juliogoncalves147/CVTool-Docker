from .CommonsHelper import sortByIndexAsc, groupBlocks
from src.writer import Writer
import re

# Check if the block has a date command
def checkTheme(block, word):
    # Use word boundaries to ensure 'word' is matched as a whole word
    word_pattern = r'\b' + re.escape(word.lower()) + r'\b'

    for item in block:
        print("ENTREEEEI")
        if item.get("tipo") == "element" and re.search(word_pattern, item.get("valor", "").lower()):
            return True
    return False

def isSectionorSubSectionBlock(block):
    for item in block:
        if item.get("tipo") == "command" and (item.get("valor") == "subsection" or item.get("valor") == "section"):
            return True
    return False

# Filter the dataBlocks by date. If the block doesnt have a date command, add it to the filtered data. If it has a date command, check the date condition.
def filterByTheme(dataBlocks, word, logicalOperator):
    filteredData = []

    for block in dataBlocks:
        hasTheme = checkTheme(block, word) # Check for a date command in the block
        if hasTheme and (logicalOperator == "="): # Check the date condition
            filteredData.extend(block)
        elif not hasTheme and (logicalOperator == "!=") : # If there is no date command, add the block to the filtered data
            filteredData.extend(block)
        elif isSectionorSubSectionBlock(block):
            filteredData.extend(block)
        else:
            continue
        
    sortedData = sortByIndexAsc(filteredData) # Sort the data by index
    
    return sortedData

# Process date query
def filterThemeQuery(parsedData, ano, logicalOperator):
    dataBlocks = groupBlocks(parsedData)
    #print(f"Filtering data by date: {ano} {logicalOperator}")
    #print(f"Data blocks: {len(dataBlocks)}")
    #print(f"Data blocks: {dataBlocks}")
    return filterByTheme(dataBlocks, ano, logicalOperator)