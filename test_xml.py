#XML Validity Tests
#By: Jean Luka Molina
#25/03/2024

import pytest
from nltk import CFG
from CYK_Parser import dictionary_creation, input_collector, cyk_parser
from Grammars import xml


#Generate the dictionary once so the process doesn't need to be repeated
cnf_xml_dict = dictionary_creation( xml.chomsky_normal_form( ).productions( ) )
@pytest.mark.parametrize( "dictionary, file, test_type, result", [( cnf_xml_dict, "FILES\\XML_Files\\xml_1.txt", "Normal Tag Test", True ),
                                                      ( cnf_xml_dict, "FILES\\XML_Files\\xml_2.txt", "Comment Test", True),
                                                      ( cnf_xml_dict, "FILES\\XML_Files\\xml_3.txt", "Normal Tag and Comment Test", True),
                                                      ( cnf_xml_dict, "FILES\\XML_Files\\xml_4.txt", "Numbers as Tag Names Test", False),
                                                      ( cnf_xml_dict, "FILES\\XML_Files\\xml_5.txt", "Spaces Between Tag Names Test", False),
                                                      ( cnf_xml_dict, "FILES\\XML_Files\\xml_6.txt", "Use of Entity References within content", True),
                                                      ( cnf_xml_dict, "FILES\\XML_Files\\xml_7.txt", "Use of Attributes", True),
                                                      ( cnf_xml_dict, "FILES\\XML_Files\\xml_8.txt", "Combine Everything", True),
                                                     ] )
def test_CYK_XML( dictionary, file, test_type, result ):
    """Tests the xml gramamr with some inputs"""
    string = input_collector( file )
    letters = list( string )

    assert ( cyk_parser( dictionary, letters ) == result )
    print( f"Test #1 ( CYK PARSING XML ) | Test Type: [{test_type}] | File: {file} | Result: {result} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------------------------------\n" )