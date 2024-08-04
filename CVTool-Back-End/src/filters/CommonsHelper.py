import unicodedata
import re

def sortByIndexAsc(data):
    return sorted(data, key=lambda x: int(x['id']))

def groupBlocks(data):
    blocks = []
    current_block = []
    start = False
    inside_block = False

    for item in data:
        if item['nivel'] == 0 and inside_block == True:
            current_block.append(item)
            blocks.append(current_block)
            current_block = []
            start = False
            inside_block = False
        elif item['nivel'] == 0 and start == False:
            start = True
            current_block.append(item)
        elif item['nivel'] == 1:
            inside_block = True
            current_block.append(item)
        else:
            current_block.append(item)
    

    return blocks

def remove_invisible_characters(parsed_file):
    
    for item in parsed_file:
    # Normalize the text to NFKD form to separate characters and their diacritics
        if item.get("valor") is not None:
            text = unicodedata.normalize('NFKD', str(item.get("valor")))
    
    # Remove combining characters (diacritics)
        text = ''.join([c for c in text if not unicodedata.combining(c)])
    
    # Define a pattern to match any non-printable characters (control characters, zero-width spaces, etc.)
        invisible_characters_pattern = re.compile(r'[\u200B-\u200D\uFEFF]')
    
    # Remove invisible characters
        item["valor"] = invisible_characters_pattern.sub('', text)
    
    return parsed_file