#HTML Validity Tests
#By: Jean Luka Molina
#25/03/2024

import pytest
from nltk import CFG
from CYK_Parser import dictionary_creation, input_collector, html_xml_input_tokenizer, cyk_parser
from Grammars import html


@pytest.mark.parametrize( "file, string", [( "FILES\\HTML_Files\\HTML_1.txt", '<html lang="en" dir="ltr"></html>' ) ] )
def test_input_collector( file, string ):
    """Tests that we get the proper input to parse"""
    file_input = input_collector( file )

    assert( file_input == string )
    print( f"Test #1 ( Valid Input Collection Test ) | File: [{file}] -> Expected Result: {string} | Result: {file_input == string} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------\n" )

@pytest.mark.parametrize( "file, tokens", [( "FILES\\HTML_Files\\HTML_2.txt", ['<', 'html', '>', '<', '/', 'html', '>'] ) ] )
def test_input_tokenizer( file, tokens ):

    file_input = input_collector( file )

    result = html_xml_input_tokenizer( file_input )
    assert( result == tokens )
    print( f"Test #2 ( Tokenizing Test ) | File: [{file}] -> Expected Result: {tokens} | Result: {result == tokens} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------\n" )

    

#Generate the dictionary once so the process doesn't need to be repeated
cnf_html_dict = dictionary_creation( html.chomsky_normal_form( ).productions( ) )
@pytest.mark.parametrize( "dictionary, file, test_type, result", [( cnf_html_dict, "FILES\\HTML_Files\\HTML_2.txt", "Normal Tag Test", True ),
                                                     ] )
def test_CYK_XML( dictionary, file, test_type, result ):
    """Tests the input strings to make sure they are valid for the language"""
    file_input = input_collector( file )

    tokens = html_xml_input_tokenizer( file_input )
    
    assert ( cyk_parser( dictionary, tokens ) == result )
    print( f"Test #3 ( CYK PARSING HTML ) | Test Type: [{test_type}] | tokens: {tokens} | Result: {result} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------------------------------\n" )