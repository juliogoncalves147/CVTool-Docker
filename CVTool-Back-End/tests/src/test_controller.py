import pytest
import logging
from parsers.dslParser import DSLParser
from controller import Controller
from parsers.cvParser import CVParser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class TestCVParser:
    
    # Test the NamedItem syntax in the CVParser
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