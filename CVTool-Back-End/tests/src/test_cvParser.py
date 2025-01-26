import pytest
import logging
from parsers.cvParser import CVParser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class TestCVParser:
    
    # Test the NamedItem syntax in the CVParser
    def test_prhCV_Parser(self):
        # Test the namedItens method
        cvParser = CVParser()
        with open('tests/resources/data/prhCV.tex', 'r') as file:
            text = file.read()
            result = cvParser.parse(text)
            
            with open('tests/resources/logs.files/prhCV_expected.json', 'w') as file2:
                file2.write(str(result))

        with open('tests/resources/assertFiles/prhCV_expected.json', 'r') as file3:
            expected = file3.read()

        
        assert str(result) == expected

    def test_mjvCV_Parser(self):
        # Test the namedItens method
        cvParser = CVParser()
        with open('tests/resources/data/mjvCV.tex', 'r') as file:
            text = file.read()
            result = cvParser.parse(text)
            
            with open('tests/resources/logs.files/mjvCV_expected.json', 'w') as file2:
                file2.write(str(result))

        with open('tests/resources/assertFiles/mjvCV_expected.json', 'r') as file3:
            expected = file3.read()

        assert str(result) == expected
        
    def test_namedItens(self):
        # Test the namedItens method
        cvParser = CVParser()
        with open('tests/resources/data/namedItens.tex', 'r') as file:
            text = file.read()
            result = cvParser.parse(text)
            
            with open('tests/resources/logs.files/namedItens_expected.json', 'w') as file2:
                file2.write(str(result))

        with open('tests/resources/assertFiles/namedItens_expected.json', 'r') as file3:
            expected = file3.read()

        logger.info(f"Parsed result: {result}")
        
        assert str(result) == expected
        
    def test_namedItens_with_sections(self):
        # Test the namedItens method
        cvParser = CVParser()
        with open('tests/resources/data/namedItens_withSection.tex', 'r') as file:
            text = file.read()
            result = cvParser.parse(text)

            with open('tests/resources/logs.files/namedItens_withSection_expected.json', 'w') as file2:
                file2.write(str(result))

        with open('tests/resources/assertFiles/namedItens_withSection_expected.json', 'r') as file3:
            expected = file3.read()
        
        
        assert str(result) == expected