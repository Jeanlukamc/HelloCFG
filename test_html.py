#HTML Validity Tests
#By: Jean Luka Molina
#25/03/2024

import pytest
from nltk import CFG
from CYK_Parser import dictionary_creation, input_collector, html_input_tokenizer, cyk_parser
from Grammars import html


@pytest.mark.parametrize( "file, string", [( "FILES\\HTML_Files\\HTML_1.txt", '<html lang="en" dir="ltr"></html>' ) ] )
def test_input_collector( file, string ):
    """Tests that we get the proper input to parse"""
    file_input = input_collector( file )

    assert( file_input == string )
    print( f"Test #1 ( Valid Input Collection Test ) | File: [{file}] -> Expected Result: {string} | Result: {file_input == string} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------\n" )

@pytest.mark.parametrize( "file, tokens", [( "FILES\\HTML_Files\\HTML_2.txt", ['<', 'html', '>', '<', '/', 'html', '>'] ),
                                           ( "FILES\\HTML_Files\\HTML_3.txt", ['<', 'html', '>', '<', 'head', '>', '<', 'title', '>', 't', 'i', 't', 'l', 'e', 'c', 'a', 'r', 'd', '<', '/', 'title', '>', '<', '/', 'head', '>', '<', 'body', '>', 't', 'e', 'x', 't', 't', 'o', 'w', 'o', 'r', 'k', 'w', 'i', 't', 'h', '<', '/', 'body', '>', '<', '/', 'html', '>'] ) ] )
def test_input_tokenizer( file, tokens ):

    file_input = input_collector( file )

    result = html_input_tokenizer( file_input )
    assert( result == tokens )
    print( f"Test #1 ( Tokenizing Test ) | File: [{file}] -> Expected Result: {tokens} | Result: {result == tokens} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------\n" )

    

#Generate the dictionary once so the process doesn't need to be repeated
cnf_html_dict = dictionary_creation( html.chomsky_normal_form( ).productions( ) )
@pytest.mark.parametrize( "dictionary, file, test_type, result", [( cnf_html_dict, "FILES\\HTML_Files\\HTML_2.txt", "Normal Tag Test", True ),
                                                                  ( cnf_html_dict, "FILES\\HTML_Files\\HTML_3.txt", "Head and Body Test", True ),
                                                                  ( cnf_html_dict, "FILES\\HTML_Files\\HTML_4.txt", "Heading 1 - 6 Test", True ),
                                                                  ( cnf_html_dict, "FILES\\HTML_Files\\HTML_5.txt", "Line Break and Horizontal Rule Test", False ),
                                                                  ( cnf_html_dict, "FILES\\HTML_Files\\HTML_6.txt", "Strong, Emphasis, and Span Test", True ),
                                                                  ( cnf_html_dict, "FILES\\HTML_Files\\HTML_7.txt", "Lists, List Items, and List Nesting Test", True ),
                                                                  ( cnf_html_dict, "FILES\\HTML_Files\\HTML_8.txt", "Using Divs Test", True ),
                                                                  ( cnf_html_dict, "FILES\\HTML_Files\\HTML_9.txt", "Form use Test", True ),
                                                                  ( cnf_html_dict, "FILES\\HTML_Files\\HTML_10.txt", "Image Attribute Test", True )] )
def test_CYK_XML( dictionary, file, test_type, result ):
    """Tests the input strings to make sure they are valid for the language"""
    file_input = input_collector( file )

    tokens = html_input_tokenizer( file_input )
    
    assert ( cyk_parser( dictionary, tokens ) == result )
    print( f"Test #2 ( CYK PARSING HTML ) | Test Type: [{test_type}] | Result: {result} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------------------------------\n" )