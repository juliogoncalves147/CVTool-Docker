import dateparser
from .CommonsHelper import sortByIndexAsc, groupBlocks
import re

# Check if the block has a date command
def checkDate(block):
    for item in block:
        if item.get("tipo") == "command" and item.get("valor") == "daterange":
            return True
    return False

# Check if the year matches the condition and logical operator
def checkYear(year, ano, logicalOperator):
    if logicalOperator == "<":
        if year < int(ano):
            return True
    if logicalOperator == ">":
        if year > int(ano):
            return True
    if logicalOperator == "<=":
        if year <= int(ano):
            return True
    if logicalOperator == ">=":
        if year >= int(ano):
            return True
    if logicalOperator == "=":
        if year == int(ano):
            return True
    return False

# Check if the block has a date that corresponds to the condition and year provided
def filterDate(block, ano, logicalOperator):
    isDateCommand = False
    for item in block:
        if item.get("tipo") == "command" and item.get("valor") == "daterange": # If we are in this context, the next item is a date. We set the flag, to process the next element for dates search.
            isDateCommand = True
        if item.get("tipo") == "element" and isDateCommand:
            # Define a regex pattern to match years in various formats
            year_pattern = re.compile(r'\b(?:\d{4}|\d{4}-\d{4}|\d{4}-\.\.\.|\(\d{4}\)|\w{3,9}, \d{4}|\d{2}-\d{2}-\d{4}|\w+\'\d{4})\b')
            # Find all matches in the text
            year_matches = year_pattern.findall(item.get("valor"))
            
            for match in year_matches: # Its gridy. If find one year in the text that is greater than the filter, automatically add the block
                # Parse the date string using dateparser
                parsed_date = dateparser.parse(match)
                if parsed_date:
                    year = parsed_date.year
                    if checkYear(year, ano, logicalOperator):
                        return True
            isDateCommand = False
    return False

# Filter the dataBlocks by date. If the block doesnt have a date command, add it to the filtered data. If it has a date command, check the date condition.
def filterByDate(dataBlocks, ano, logicalOperator):
    filteredData = []
    
    for block in dataBlocks:
        hasDate = checkDate(block) # Check for a date command in the block
        if hasDate: # Check the date condition
            addBlock = filterDate(block, ano, logicalOperator)
            if addBlock:
                filteredData.extend(block)
        else: # If there is no date command, add the block to the filtered data
            filteredData.extend(block)
    
    sortedData = sortByIndexAsc(filteredData) # Sort the data by index
    
    return sortedData

# Process date query
def filterDateQuery(parsedData, ano, logicalOperator):
    dataBlocks = groupBlocks(parsedData)
    #print(f"Filtering data by date: {ano} {logicalOperator}")
    #print(f"Data blocks: {len(dataBlocks)}")
    #print(f"Data blocks: {dataBlocks}")
    return filterByDate(dataBlocks, ano, logicalOperator)