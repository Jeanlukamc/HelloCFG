#Morse Validity Tests
#By: Jean Luka Molina
#25/03/2024

import pytest
from nltk import CFG
from CYK_Parser import dictionary_creation, cyk_parser
from morse_to_language import english_equivalent, morse_english_input_collector
from langauge_to_morse import morse_code_equivalent, edit_morse_file_equivalent, morse_tokenizer
from Grammars import morse_grammar

test = False

@pytest.mark.skipif( test == True, reason="Don't want to test right now!" )
@pytest.mark.parametrize( "file, string", [( "FILES\\Morse_Code_Files\\english_1.txt", 'WELCOME TO THE 1ST TEST' ),
                                           ( "FILES\\Morse_Code_Files\\english_2.txt", '( ALPHA <MULT> (BETA <ADD> CHARLIE) ) <POWER> ( ALPHA <DIV> (BETA <SUB> CHARLIE) )' ),
                                           ( "FILES\\Morse_Code_Files\\english_3.txt", 'VAR <EQUALS><EQUALS> ( A <MULT> B ) VAR2 <EQUALS> VAR <ADD> 2 <CONST> _CONST <EQUALS> "TEXT" <CONST> T_1 <EQUALS> 55' ),
                                           ( "FILES\\Morse_Code_Files\\english_4.txt", '<PRINT>("OMG" ) <PRINT>(5) <PRINT>( V1 ) <PRINT>( "M" <ADD> 5) <PRINT>( V1 <ADD> "50C" )' ),
                                           ( "FILES\\Morse_Code_Files\\english_5.txt", '<IF> (A <EQUALS><EQUALS> B): { <PRINT> ( "WIN" ) }  <IF> "T" <EQUALS><EQUALS> "T": { <PRINT> ( "WIN" ) } <ELSE> : { <PRINT> ( "LOSE" ) }' ) ] )
def test_input_collector( file, string ):
    """Tests that we get the proper input to parse"""
    file_input = morse_english_input_collector( file )

    assert( file_input == string )
    print( f"Test #1 ( Valid Input Collection Test ) | File: [{file}] -> Expected Result: {string} | Result: {file_input == string} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------\n" )

@pytest.mark.skipif( test == True, reason="Don't want to test right now!" )
@pytest.mark.parametrize( "file, string", [( "FILES\\Morse_Code_Files\\english_1.txt", 'WELCOME TO THE 1ST TEST' ),
                                           ( "FILES\\Morse_Code_Files\\english_2.txt", '(  ALPHA <MULT>  ( BETA <ADD>  CHARLIE)  )  <POWER>  (  ALPHA <DIV>  ( BETA <SUB>  CHARLIE)  )' ),
                                           ( "FILES\\Morse_Code_Files\\english_3.txt", 'VAR <EQUALS> <EQUALS>  (  A <MULT>  B )  VAR2 <EQUALS>  VAR <ADD>  2 <CONST>  _ CONST <EQUALS>  " TEXT"  <CONST>  T_ 1 <EQUALS>  55' ),
                                           ( "FILES\\Morse_Code_Files\\english_4.txt", '<PRINT> ( " OMG"  )  <PRINT> ( 5)  <PRINT> (  V1 )  <PRINT> (  " M"  <ADD>  5)  <PRINT> (  V1 <ADD>  " 50C"  )' ),
                                           ( "FILES\\Morse_Code_Files\\english_5.txt", '<IF>  ( A <EQUALS> <EQUALS>  B) :  {  <PRINT>  (  " WIN"  )  }   <IF>  " T"  <EQUALS> <EQUALS>  " T" :  {  <PRINT>  (  " WIN"  )  }  <ELSE>  :  {  <PRINT>  (  " LOSE"  )  }' ) ] )
def test_language_to_morse_to_language_translation( file, string ):
    """Tests that the conversion from english to morse makes sense when translated back"""
    file_input = morse_english_input_collector( file )

    morse_sentence = morse_code_equivalent( file_input )
    english_sentence = english_equivalent( morse_sentence )

    assert( english_sentence == string )
    print( f"Test #2 ( English -> Morse -> English ) | File: [{file}] -> Expected Result: {string} | Result: {english_sentence == string} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------\n" )

@pytest.mark.skipif( test == True, reason="Don't want to test right now!" )
@pytest.mark.parametrize( "file_1, file_2, string", [( "FILES\\Morse_Code_Files\\english_1.txt", "FILES\\Morse_Code_Files\\morse_1.txt", '.--#.#.-..#-.-.#---#--#.#/-#---#/-#....#.#/.----#...#-#/-#.#...#-#/' ),
                                                     ( "FILES\\Morse_Code_Files\\english_2.txt", "FILES\\Morse_Code_Files\\morse_2.txt", '(#//.-#.-..#.--.#....#.-#/<#--#..-#.-..#-#>#//(#/-...#.#-#.-#/<#.-#-..#-..#>#//-.-.#....#.-#.-.#.-..#..#.#)#//)#//<#.--.#---#.--#.#.-.#>#//(#//.-#.-..#.--.#....#.-#/<#-..#..#...-#>#//(#/-...#.#-#.-#/<#...#..-#-...#>#//-.-.#....#.-#.-.#.-..#..#.#)#//)#//' ),
                                                     ( "FILES\\Morse_Code_Files\\english_3.txt", "FILES\\Morse_Code_Files\\morse_3.txt", '...-#.-#.-.#/<#.#--.-#..-#.-#.-..#...#>#/<#.#--.-#..-#.-#.-..#...#>#//(#//.-#/<#--#..-#.-..#-#>#//-...#/)#//...-#.-#.-.#..---#/<#.#--.-#..-#.-#.-..#...#>#//...-#.-#.-.#/<#.-#-..#-..#>#//..---#/<#-.-.#---#-.#...#-#>#//_#/-.-.#---#-.#...#-#/<#.#--.-#..-#.-#.-..#...#>#//"#/-#.#-..-#-#"#//<#-.-.#---#-.#...#-#>#//-#_#/.----#/<#.#--.-#..-#.-#.-..#...#>#//.....#.....#/' ),
                                                     ( "FILES\\Morse_Code_Files\\english_4.txt", "FILES\\Morse_Code_Files\\morse_4.txt", '<#.--.#.-.#..#-.#-#>#/(#/"#/---#--#--.#"#//)#//<#.--.#.-.#..#-.#-#>#/(#/.....#)#//<#.--.#.-.#..#-.#-#>#/(#//...-#.----#/)#//<#.--.#.-.#..#-.#-#>#/(#//"#/--#"#//<#.-#-..#-..#>#//.....#)#//<#.--.#.-.#..#-.#-#>#/(#//...-#.----#/<#.-#-..#-..#>#//"#/.....#-----#-.-.#"#//)#//' ),
                                                     ( "FILES\\Morse_Code_Files\\english_5.txt", "FILES\\Morse_Code_Files\\morse_5.txt", '<#..#..-.#>#//(#/.-#/<#.#--.-#..-#.-#.-..#...#>#/<#.#--.-#..-#.-#.-..#...#>#//-...#)#/:#//{#//<#.--.#.-.#..#-.#-#>#//(#//"#/.--#..#-.#"#//)#//}#///<#..#..-.#>#//"#/-#"#//<#.#--.-#..-#.-#.-..#...#>#/<#.#--.-#..-#.-#.-..#...#>#//"#/-#"#/:#//{#//<#.--.#.-.#..#-.#-#>#//(#//"#/.--#..#-.#"#//)#//}#//<#.#.-..#...#.#>#//:#//{#//<#.--.#.-.#..#-.#-#>#//(#//"#/.-..#---#...#.#"#//)#//}#//' ) ] )
def test_make_morse_file_equivalent( file_1, file_2, string ):
    """Tests that we have created an equivalent morse file from the english version"""
    my_input = morse_english_input_collector( file_1 )
    morse =  morse_code_equivalent( my_input )
    edit_morse_file_equivalent( file_2, morse )

    my_input = morse_english_input_collector( file_2 )
    assert( my_input == string )
    print( f"Test #3 ( Morse File Equivalent Maker Test ) | File: [{file_1}] -> File To Write: {file_2} | Result: {my_input == string} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------\n" )


cnf_morse_dict = dictionary_creation( morse_grammar.chomsky_normal_form( ).productions( ) )
@pytest.mark.parametrize( "dictionary, file, test_type, result",  [ ( cnf_morse_dict, "FILES\\Morse_Code_Files\\morse_1.txt", "Alphabet and Letters Test", True ),
                                                                    ( cnf_morse_dict, "FILES\\Morse_Code_Files\\morse_2.txt", "Basic Math Operations Test", True ),
                                                                    ( cnf_morse_dict, "FILES\\Morse_Code_Files\\morse_3.txt", "Comparison, Assignment, Constants, and Multi-Line Test", True ),
                                                                    ( cnf_morse_dict, "FILES\\Morse_Code_Files\\morse_4.txt", "Printing Test", True ),
                                                                    ( cnf_morse_dict, "FILES\\Morse_Code_Files\\morse_5.txt", "If-Else Statement Tests", True )  ] )
def test_CYK_XML( dictionary, file, test_type, result ):
    """Tests the input strings to make sure they are valid for the language"""

    file_input = morse_english_input_collector( file )
    tokens = morse_tokenizer( file_input )

    assert ( cyk_parser( dictionary, tokens ) == result )
    print( f"Test #4 ( CYK PARSING Morse Code ) | Test Type: [{test_type}] | Result: {result} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------------------------------\n" )
    
