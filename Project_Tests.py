#Tests
#By: Jean Luka Molina
#25/03/2024

import pytest
from nltk import CFG
from CYK_Parser import valid_CFG, conversion_to_CNF, dictionary_creation, cyk_parser
from Grammars import xml, invalid_CNF_grammar, basic_grammar


@pytest.mark.parametrize( "grammar, test_num, result", [ ( xml, 1, True ), (invalid_CNF_grammar, 2, True), (basic_grammar, 3, True) ] )
def test_valid_CFG( grammar, test_num, result):
    """Test the validity of the grammar"""
    assert( valid_CFG( grammar ) == result )
    for item in grammar.productions( ):
        print( item )
    print( f"Test #1 ( VALID CFG ) | Languege #{test_num} Result: {result} | PASSED")
    print( "----------------------------------------------------------------------------------------------------\n" )

@pytest.mark.parametrize( "grammar, test_num, result", [ ( xml, 1, True ), (invalid_CNF_grammar, 2, False), (basic_grammar, 3, True)] )
def test_CNF_conversion( grammar, test_num, result ):
    """Tests whether a CFG can be turned into a CNF"""
    assert( conversion_to_CNF( grammar ) == result )
    if ( result ):
        for item in grammar.chomsky_normal_form( ).productions( ):
            print( item )
    print( f"Test #2 ( VALID CNF CONVERSION ) | Languege #{test_num} Result: {result} | PASSED")
    print( "----------------------------------------------------------------------------------------------------\n" )


@pytest.mark.parametrize( "grammar, strings, test_num, results", [( basic_grammar,
                                                                [
                                                                    "the cat chases the dog",
                                                                    "a dog sees the cat",
                                                                    "the dog chases the dog",
                                                                    "the cat sleeps the dog",
                                                                    "dog chases cat",
                                                                    "the dog on in the park",
                                                                    "chases the dog the cat"
                                                                ],
                                                                1,
                                                                [ True,
                                                                  True,
                                                                  True,
                                                                  False,
                                                                  False,
                                                                  False,
                                                                  False
                                                                ] ) ])
def test_CYK_parser( grammar, strings, test_num, results ):
    """Tests the CYK parser for string validity"""
    rule_dict = dictionary_creation( grammar.chomsky_normal_form( ).productions( ) )

    for string in range( 0, len( strings )):
        words = strings[ string ].split( )
        assert ( cyk_parser( rule_dict, words ) == results[ string ] )
        print( f"Test #3 ( CYK PARSING ) | Languege #{test_num} Result: {results[ string ]} | PASSED")
        print( "----------------------------------------------------------------------------------------------------\n" )

