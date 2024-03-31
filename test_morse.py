#Morse Validity Tests
#By: Jean Luka Molina
#25/03/2024

import pytest
from nltk import CFG
from CYK_Parser import dictionary_creation, cyk_parser
from morse_to_language import english_equivalent, morse_english_input_collector
from langauge_to_morse import morse_code_equivalent, edit_morse_file_equivalent, morse_tokenizer

@pytest.mark.parametrize( "file, string", [( "FILES\\Morse_Code_Files\\english_1.txt", '<WHILE> ( ALPHA <SUB> BETA <EQUALS><EQUALS> 15 )' ) ] )
def test_input_collector( file, string ):
    """Tests that we get the proper input to parse"""
    file_input = morse_english_input_collector( file )

    assert( file_input == string )
    print( f"Test #1 ( Valid Input Collection Test ) | File: [{file}] -> Expected Result: {string} | Result: {file_input == string} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------\n" )

@pytest.mark.parametrize( "file, string", [( "FILES\\Morse_Code_Files\\english_1.txt", '<WHILE> ( ALPHA <SUB> BETA <EQUALS><EQUALS> 15 )' ) ] )
def test_language_to_morse_to_language_translation( file, string ):
    """Tests that the conversion from english to morse makes sense when translated back"""
    file_input = morse_english_input_collector( file )

    morse_sentence = morse_code_equivalent( file_input )
    english_sentence = english_equivalent( morse_sentence )

    assert( english_sentence == string )
    print( f"Test #2 ( English -> Morse -> English ) | File: [{file}] -> Expected Result: {string} | Result: {english_sentence == string} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------\n" )

@pytest.mark.parametrize( "file_1, file_2, string", [( "FILES\\Morse_Code_Files\\english_1.txt", "FILES\\Morse_Code_Files\\morse_1.txt", "<#.--#....#..#.-..#.#>#/(#/.-#.-..#.--.#....#.-#/<#...#..-#-...#>#/-...#.#-#.-#/<#.#--.-#..-#.-#.-..#...#>#<#.#--.-#..-#.-#.-..#...#>#/.----#.....#/)#/" ) ] )
def test_make_morse_file_equivalent( file_1, file_2, string ):
    """Tests that we have created an equivalent morse file from the english version"""
    my_input = morse_english_input_collector( file_1 )
    morse =  morse_code_equivalent( my_input )
    edit_morse_file_equivalent( file_2, morse )

    my_input = morse_english_input_collector( file_2 )
    assert( my_input == string )
    print( f"Test #3 ( Morse File Equivalent Maker Test ) | File: [{file_1}] -> File To Write: {file_2} | Result: {my_input == string} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------\n" )