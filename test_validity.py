#Validiy, File Reading, and Conversion Tests
#By: Jean Luka Molina
#25/03/2024

import pytest
from nltk import CFG
from CYK_Parser import valid_CFG, conversion_to_CNF, input_collector, dictionary_creation, cyk_parser
from Grammars import xml, invalid_CNF_grammar, basic_grammar


@pytest.mark.parametrize( "grammar, test_num, result", [ ( xml, 1, True ), (invalid_CNF_grammar, 2, True), (basic_grammar, 3, True) ] )
def test_valid_CFG( grammar, test_num, result):
    """Test the validity of the grammar"""
    assert( valid_CFG( grammar ) == result )
    for item in grammar.productions( ):
        print( item )
    print( f"Test #1 ( VALID CFG ) | Languege #{test_num} Result: {result} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------\n" )

@pytest.mark.parametrize( "grammar, test_num, result", [ ( xml, 1, True ), (invalid_CNF_grammar, 2, False), (basic_grammar, 3, True)] )
def test_CNF_conversion( grammar, test_num, result ):
    """Tests whether a CFG can be turned into a CNF"""
    assert( conversion_to_CNF( grammar ) == result )
    if ( result ):
        for item in grammar.chomsky_normal_form( ).productions( ):
            print( item )
    print( f"Test #2 ( VALID CNF CONVERSION ) | Languege #{test_num} Result: {result} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------\n" )

@pytest.mark.parametrize( "file, string", [ ( "FILES\\Basic_Grammar_Files\\1.txt",  "the cat chases the dog"),
                                            ( "FILES\\XML_Files\\xml_8.txt", "<TopLayer id=\"501\"><SecondLayer test=\"8\">Test 1 &lt; Test 2</SecondLayer></TopLayer>" ),
                                            ( "FILES\\HTML_Files\\HTML_2.txt", '<   html ></ html>') ] )
def test_input_collector( file, string ):
    """Tests that we get the proper input to parse"""
    file_input = input_collector( file )

    assert( file_input == string )
    print( f"Test #3 ( Valid Input Collection Test ) | File: [{file}] -> Expected Result: {string} | Result: {file_input == string} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------\n" )

@pytest.mark.parametrize( "grammar, string, result", [  ( basic_grammar, "the cat chases the dog", True ),
                                                                    ( basic_grammar, "a dog sees the cat", True ),
                                                                    ( basic_grammar, "the dog chases the dog", True ),
                                                                    ( basic_grammar, "the cat sleeps the dog", False ),
                                                                    ( basic_grammar, "dog chases cat", False ),
                                                                    ( basic_grammar, "the dog on in the park", False ),
                                                                    ( basic_grammar, "chases the dog the cat", False )
                                                                ] )
def test_CYK_parser_per_word( grammar, string, result ):
    """Tests the CYK parser for string validity"""
    rule_dict = dictionary_creation( grammar.chomsky_normal_form( ).productions( ) )

    words = string.split( )

    assert ( cyk_parser( rule_dict, words ) == result )
    print( f"Test #4 ( CYK PARSING PER WORD ) | String: {string} | Result: {result} | PASSED")
    print( "--------------------------------------------------------------------------------------------------------------------------------------\n" )