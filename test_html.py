#HTML Validity Tests
#By: Jean Luka Molina
#25/03/2024

import pytest
from nltk import CFG
from CYK_Parser import dictionary_creation, input_collector, cyk_parser
from Grammars import html


@pytest.mark.parametrize( "file, string", [( "FILES\\HTML_Files\\HTML_1.txt", '<html lang="en" dir="ltr"></html>' ) ] )
def test_input_collector( file, string ):
    """Tests that we get the proper input to parse"""
    file_input = input_collector( file )

    assert( file_input == string )
    print( f"Test #3 ( Valid Input Collection Test ) | File: [{file}] -> Expected Result: {string} | Result: {file_input == string} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------\n" )

#Generate the dictionary once so the process doesn't need to be repeated
cnf_html_dict = dictionary_creation( html.chomsky_normal_form( ).productions( ) )
@pytest.mark.parametrize( "dictionary, string, test_type, result", [( cnf_html_dict, "<html></html>", "Normal Tag Test", True ),
                                                      ( cnf_html_dict, "<!-- Welcome To The Jungle   -->", "Comment Test", True)
                                                     ] )
def test_CYK_XML( dictionary, string, test_type, result ):
    """Tests the input strings to make sure they are valid for the language"""