import pytest
from parsers.cvParser import CVParser

class TestCVParser:
    
    # Test the NamedItem syntax in the CVParser
    def test_namedItens(self):
        # Test the namedItens method
        cvParser = CVParser()
        with open('tests/resources/data/namedItens.tex', 'r') as file:
            text = file.read()
            result = cvParser.parse(text)
        
        assert result == [{'id': '1', 'tipo': 'command', 'valor': 'namedItem', 'nivel': 0, 'section': ''}, 
                        {'id': '2', 'tipo': 'element', 'valor': "[SAC'2013-PL]", 'nivel': 0, 'section': '', 'reserved': False},
                        {'id': '3', 'tipo': 'LB', 'valor': '{', 'nivel': 0, 'section': ''},
                        {'id': '4', 'tipo': 'element', 'valor': 'ACM-SIGAPP ', 'nivel': 1, 'section': '', 'reserved': False},
                        {'id': '5', 'tipo': 'command', 'valor': 'emph', 'nivel': 1, 'section': ''},
                        {'id': '6', 'tipo': 'LB', 'valor': '{', 'nivel': 1, 'section': ''},
                        {'id': '7', 'tipo': 'element', 'valor': 'Symposium on Applied Computing -- Technical Track on "Programming Languages"', 'nivel': 2, 'section': '', 'reserved': False},
                        {'id': '8', 'tipo': 'RB', 'valor': '}', 'nivel': 1, 'section': ''},
                        {'id': '9', 'tipo': 'element', 'valor': ', Coimbra/Portugal, March 2013.', 'nivel': 1, 'section': '', 'reserved': False},
                        {'id': '10', 'tipo': 'RB', 'valor': '}', 'nivel': 0, 'section': ''},
                        {'id': '11', 'tipo': 'command', 'valor': 'namedItem', 'nivel': 0, 'section': ''},
                        {'id': '12', 'tipo': 'element', 'valor': "[SLATe'2013]", 'nivel': 0, 'section': '', 'reserved': False},
                        {'id': '13', 'tipo': 'LB', 'valor': '{', 'nivel': 0, 'section': ''},
                        {'id': '14', 'tipo': 'element', 'valor': '2nd ', 'nivel': 1, 'section': '', 'reserved': False},
                        {'id': '15', 'tipo': 'command', 'valor': 'emph', 'nivel': 1, 'section': ''},
                        {'id': '16', 'tipo': 'LB', 'valor': '{', 'nivel': 1, 'section': ''},
                        {'id': '17', 'tipo': 'element', 'valor': 'Symposium on Languages, Applications and Tools', 'nivel': 2, 'section': '', 'reserved': False},
                        {'id': '18', 'tipo': 'RB', 'valor': '}', 'nivel': 1, 'section': ''},
                        {'id': '19', 'tipo': 'element', 'valor': ', Porto/Portugal, June 2013.', 'nivel': 1, 'section': '', 'reserved': False},
                        {'id': '20', 'tipo': 'RB', 'valor': '}', 'nivel': 0, 'section': ''},
                        {'id': '21', 'tipo': 'command', 'valor': 'namedItem', 'nivel': 0, 'section': ''},
                        {'id': '22', 'tipo': 'element', 'valor': "[SCLIT'2013]", 'nivel': 0, 'section': '', 'reserved': False},
                        {'id': '23', 'tipo': 'LB', 'valor': '{', 'nivel': 0, 'section': ''},
                        {'id': '24', 'tipo': 'element', 'valor': '3rd ', 'nivel': 1, 'section': '', 'reserved': False},
                        {'id': '25', 'tipo': 'command', 'valor': 'emph', 'nivel': 1, 'section': ''},
                        {'id': '26', 'tipo': 'LB', 'valor': '{', 'nivel': 1, 'section': ''},
                        {'id': '27', 'tipo': 'element', 'valor': 'Symposium on Computer Languages, Implementation and Tools', 'nivel': 2, 'section': '', 'reserved': False},
                        {'id': '28', 'tipo': 'RB', 'valor': '}', 'nivel': 1, 'section': ''},
                        {'id': '29', 'tipo': 'element', 'valor': ', Greece, September 2013.', 'nivel': 1, 'section': '', 'reserved': False},
                        {'id': '30', 'tipo': 'RB', 'valor': '}', 'nivel': 0, 'section': ''}]
        
        
    def test_namedItens_with_sections(self):
        # Test the namedItens method
        cvParser = CVParser()
        with open('tests/resources/data/namedItens_withSection.tex', 'r') as file:
            text = file.read()
            result = cvParser.parse(text)
        
        assert result == [{'id': '1', 'tipo': 'command', 'valor': 'namedItem', 'nivel': 0, 'section': ''}, 
                        {'id': '2', 'tipo': 'element', 'valor': "[SAC'2013-PL]", 'nivel': 0, 'section': '', 'reserved': False},
                        {'id': '3', 'tipo': 'LB', 'valor': '{', 'nivel': 0, 'section': ''},
                        {'id': '4', 'tipo': 'element', 'valor': 'ACM-SIGAPP ', 'nivel': 1, 'section': '', 'reserved': False},
                        {'id': '5', 'tipo': 'command', 'valor': 'emph', 'nivel': 1, 'section': ''},
                        {'id': '6', 'tipo': 'LB', 'valor': '{', 'nivel': 1, 'section': ''},
                        {'id': '7', 'tipo': 'element', 'valor': 'Symposium on Applied Computing -- Technical Track on "Programming Languages"', 'nivel': 2, 'section': '', 'reserved': False},
                        {'id': '8', 'tipo': 'RB', 'valor': '}', 'nivel': 1, 'section': ''},
                        {'id': '9', 'tipo': 'element', 'valor': ', Coimbra/Portugal, March 2013.', 'nivel': 1, 'section': '', 'reserved': False},
                        {'id': '10', 'tipo': 'RB', 'valor': '}', 'nivel': 0, 'section': ''},
                        {'id': '11', 'tipo': 'command', 'valor': 'namedItem', 'nivel': 0, 'section': ''},
                        {'id': '12', 'tipo': 'element', 'valor': "[SLATe'2013]", 'nivel': 0, 'section': '', 'reserved': False},
                        {'id': '13', 'tipo': 'LB', 'valor': '{', 'nivel': 0, 'section': ''},
                        {'id': '14', 'tipo': 'element', 'valor': '2nd ', 'nivel': 1, 'section': '', 'reserved': False},
                        {'id': '15', 'tipo': 'command', 'valor': 'emph', 'nivel': 1, 'section': ''},
                        {'id': '16', 'tipo': 'LB', 'valor': '{', 'nivel': 1, 'section': ''},
                        {'id': '17', 'tipo': 'element', 'valor': 'Symposium on Languages, Applications and Tools', 'nivel': 2, 'section': '', 'reserved': False},
                        {'id': '18', 'tipo': 'RB', 'valor': '}', 'nivel': 1, 'section': ''},
                        {'id': '19', 'tipo': 'element', 'valor': ', Porto/Portugal, June 2013.', 'nivel': 1, 'section': '', 'reserved': False},
                        {'id': '20', 'tipo': 'RB', 'valor': '}', 'nivel': 0, 'section': ''},
                        {'id': '21', 'tipo': 'command', 'valor': 'section', 'nivel': 0, 'section': ''},
                        {'id': '22', 'tipo': 'LB', 'valor': '{', 'nivel': 0, 'section': ''},
                        {'id': '23', 'tipo': 'element', 'valor': 'Conferences', 'nivel': 1, 'section': 'Conferences', 'reserved': False},
                        {'id': '24', 'tipo': 'RB', 'valor': '}', 'nivel': 0, 'section': 'Conferences'},
                        {'id': '25', 'tipo': 'command', 'valor': 'namedItem', 'nivel': 0, 'section': 'Conferences'},
                        {'id': '26', 'tipo': 'element', 'valor': "[SCLIT'2013]", 'nivel': 0, 'section': 'Conferences', 'reserved': False},
                        {'id': '27', 'tipo': 'LB', 'valor': '{', 'nivel': 0, 'section': 'Conferences'},
                        {'id': '28', 'tipo': 'element', 'valor': '3rd ', 'nivel': 1, 'section': 'Conferences', 'reserved': False},
                        {'id': '29', 'tipo': 'command', 'valor': 'emph', 'nivel': 1, 'section': 'Conferences'},
                        {'id': '30', 'tipo': 'LB', 'valor': '{', 'nivel': 1, 'section': 'Conferences'},
                        {'id': '31', 'tipo': 'element', 'valor': 'Symposium on Computer Languages, Implementation and Tools', 'nivel': 2, 'section': 'Conferences', 'reserved': False},
                        {'id': '32', 'tipo': 'RB', 'valor': '}', 'nivel': 1, 'section': 'Conferences'},
                        {'id': '33', 'tipo': 'element', 'valor': ', Greece, September 2013.', 'nivel': 1, 'section': 'Conferences', 'reserved': False},
                        {'id': '34', 'tipo': 'RB', 'valor': '}', 'nivel': 0, 'section': 'Conferences'}]