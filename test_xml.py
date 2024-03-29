#XML Validity Tests
#By: Jean Luka Molina
#25/03/2024

import pytest
from nltk import CFG
from CYK_Parser import dictionary_creation, cyk_parser
from Grammars import xml, invalid_CNF_grammar, basic_grammar


#Generate the dictionary once so the process doesn't need to be repeated
cnf_xml_dict = dictionary_creation( xml.chomsky_normal_form( ).productions( ) )
@pytest.mark.parametrize( "dictionary, string, test_type, result", [( cnf_xml_dict, "<CustomTag> Testing Letters and 12345 </CustomTag>", "Normal Tag Test", True ),
                                                      ( cnf_xml_dict, "<!-- Welcome To The Jungle   -->", "Comment Test", True),
                                                      ( cnf_xml_dict, "<b><!-- test comment --><d> content </d></b>", "Normal Tag and Comment Test", True),
                                                      ( cnf_xml_dict, "<123> text </123>", "Numbers as Tag Names Test", False),
                                                      ( cnf_xml_dict, "< space > text </ space >", "Spaces Between Tag Names Test", False),
                                                      ( cnf_xml_dict, "<b>  comparison &lt;&gt;&amp;&apos;&quot; </b>", "Use of Entity References within content", True),
                                                      ( cnf_xml_dict, "<b id=\"501\" message=\"Hello World\"></b>", "Use of Attributes", True),
                                                      ( cnf_xml_dict, "<TopLayer id=\"501\"><SecondLayer test=\"8\">Test 1 &lt; Test 2</SecondLayer></TopLayer>", "Combine Everything", True),
                                                     ] )
def test_CYK_XML( dictionary, string, test_type, result ):
    """Tests the xml gramamr with some inputs"""
    letters = list( string )

    assert ( cyk_parser( dictionary, letters ) == result )
    print( f"Test #1 ( CYK PARSING XML ) | Test Type: [{test_type}] | String: {string} | Result: {result} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------------------------------\n" )