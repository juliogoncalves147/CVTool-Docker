import pytest
import logging
from parsers.dslParser import DSLParser
from controller import Controller
from parsers.cvParser import CVParser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class TestQueryParser:
    # Test the NamedItem syntax in the CVParser
    def test_SELECT(self):
        # Test the namedItens method
        dslParser = DSLParser()
        
        query = "SHOW *"

        queryResult = dslParser.parse(query)

        assert queryResult == [{'queryField': 'SHOW', 'clauses': '', 'sectionlist': ['ALL']}]

    def test_namedItens(self):
        # Test the namedItens method
        dslParser = DSLParser()
        
        query = "show * filtered by SECTION = 'Education'"

        queryResult = dslParser.parse(query)

        assert queryResult == [{'queryField': 'SHOW', 'clauses': [{'field': 'SECTION', 'operator': '=', 'value': 'Education'}], 'sectionlist': ['ALL']}]
    
    def test_namedItens_with_sections(self):
        # Test the namedItens method
        dslParser = DSLParser()
        
        query = "shOw * fiLTered By SECTION = 'Education' AND DATE > '2010' OR SECTION = 'Professional Experience' AND DATE < '2010'"

        queryResult = dslParser.parse(query)

        assert queryResult == [{'queryField': 'SHOW', 'clauses': [{'field': 'SECTION', 'operator': '=', 'value': 'Education'}, {'field': 'DATE', 'operator': '>', 'value': '2010'}, {'field': 'SECTION', 'operator': '=', 'value': 'Professional Experience'}, {'field': 'DATE', 'operator': '<', 'value': '2010'}], 'sectionlist': ['ALL']}]

