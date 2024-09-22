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


    def test_controller_query1(self):

        dslParser = DSLParser()
        cvParser = CVParser()
        controller = Controller()

        query = "SHOW * FILTERED BY (SECTION = 'Education and training' AND DATE > '2010') or (SECTION = 'Work experience' AND DATE < '2010')"

        queryResult = dslParser.parse(query)

        with open('tests/resources/data/prhCV.tex', 'r') as file:
            text = file.read()
            cvResult = cvParser.parse(text)

        result = controller.treat_query(queryResult, cvResult)

        with open('tests/resources/logs.files/prhCV_query1_expected.json', 'w') as file2:
            file2.write(str(result))

        with open('tests/resources/assertFiles/prhCV_query1_expected.json', 'r') as file3:
            expected = file3.read()

        
        assert str(result) == expected


    def test_controller_query2(self):

        dslParser = DSLParser()

        cvParser = CVParser()

        controller = Controller()

        query = "show * filtered by section = 'Work experience'"

        queryResult = dslParser.parse(query)

        with open('tests/resources/data/prhCV.tex', 'r') as file:
            text = file.read()
            cvResult = cvParser.parse(text)


        result = controller.treat_query(queryResult, cvResult)

        with open('tests/resources/logs.files/prhCV_query2_expected.json', 'w') as file2:
            file2.write(str(result))

        with open('tests/resources/assertFiles/prhCV_query2_expected.json', 'r') as file3:
            expected = file3.read()

        
        assert str(result) == expected

    def test_controller_query3(self):
            
            dslParser = DSLParser()
            cvParser = CVParser()
            controller = Controller()
    
            query = "show * fiLtered by subSection = 'Academic education' aNd daTe < '2010' or subsection = 'PhD' and date > '2010'"
    
            queryResult = dslParser.parse(query)
    
            with open('tests/resources/data/fileTest.tex', 'r') as file:
                text = file.read()
                cvResult = cvParser.parse(text)
    
    
            result = controller.treat_query(queryResult, cvResult)
    
            with open('tests/resources/logs.files/prhCV_query3_expected.json', 'w') as file2:
                file2.write(str(result))
    
            with open('tests/resources/assertFiles/prhCV_query3_expected.json', 'r') as file3:
                expected = file3.read()
    
            
            assert str(result) == expected

    def test_controller_query4(self):
                
                dslParser = DSLParser()
                cvParser = CVParser()
                controller = Controller()
        
                query = "show 'Work experience', 'Education and training' fiLtered by subSection = 'Academic education' aNd daTe < '2010' or subsection = 'PhD' and date > '2010'"
        
                queryResult = dslParser.parse(query)
        
                with open('tests/resources/data/fileTest.tex', 'r') as file:
                    text = file.read()
                    cvResult = cvParser.parse(text)
        
        
                result = controller.treat_query(queryResult, cvResult)
        
                with open('tests/resources/logs.files/prhCV_query4_expected.json', 'w') as file2:
                    file2.write(str(result))
        
                with open('tests/resources/assertFiles/prhCV_query4_expected.json', 'r') as file3:
                    expected = file3.read()
        
                
                assert str(result) == expected

