#Morse Validity Tests
#By: Jean Luka Molina
#25/03/2024

import pytest
from nltk import CFG
from CYK_Parser import dictionary_creation, input_collector, html_input_tokenizer, cyk_parser
from morse_to_language import english_equivalent
from langauge_to_morse import morse_code_equivalent

@pytest.mark.parametrize( "file, string", [( "FILES\\Morse_Code_Files\\morse_input_grab.txt", 'ALPHA - BETA = 15' ) ] )
def test_input_collector( file, string ):
    """Tests that we get the proper input to parse"""
    file_input = input_collector( file ).upper( )

    assert( file_input == string )
    print( f"Test #1 ( Valid Input Collection Test ) | File: [{file}] -> Expected Result: {string} | Result: {file_input == string} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------\n" )

@pytest.mark.parametrize( "file, string", [( "FILES\\Morse_Code_Files\\morse_input_grab.txt", 'ALPHA <SUB> BETA <EQUALS> 15' ) ] )
def test_language_to_morse_to_language_translation( file, string ):
    """Tests that the conversion from english to morse makes sense when translated back"""
    file_input = input_collector( file ).upper( )

    morse_sentence = morse_code_equivalent( file_input )
    english_sentence = english_equivalent( morse_sentence )

    assert( english_sentence == string )
    print( f"Test #2 ( English -> Morse -> English ) | File: [{file}] -> Expected Result: {string} | Result: {file_input == string} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------\n" )