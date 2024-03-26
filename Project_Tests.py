#Tests
#By: Jean Luka Molina
#25/03/2024

import pytest
from CYK_Parser import valid_CFG, conversion_to_CNF, dictionary_creation, cyk_parser
from Grammars import xml, invalid_CNF_grammar, basic_grammar


@pytest.mark.parametrize( "grammar, test_num, result", [ ( xml, 1, True ), (invalid_CNF_grammar, 2, True), (basic_grammar, 3, True) ] )
def test_valid_CFG( grammar, test_num, result):
    """Test the validity of the grammar"""
    assert( valid_CFG( grammar ) == result )
    for item in grammar.productions( ):
        print( item )
    print( f"Test #1 | Languege #{test_num} Result: {result} | PASSED")
    print( "----------------------------------------------------------------------------------------------------\n" )

@pytest.mark.parametrize( "grammar, test_num, result", [ ( xml, 1, True ), (invalid_CNF_grammar, 2, False), (basic_grammar, 3, True)] )
def test_CNF_conversion( grammar, test_num, result ):
    """Tests whether a CFG can be turned into a CNF"""
    assert( conversion_to_CNF( grammar ) == result )
    if ( result ):
        for item in grammar.chomsky_normal_form( ).productions( ):
            print( item )
    print( f"Test #2 | Languege #{test_num} Result: {result} | PASSED")
    print( "----------------------------------------------------------------------------------------------------\n" )


#@pytest.mark.parametrize( "grammar, test_num, result", [ (basic_grammar, 1, True)) ] )
#def test_rule_dictionary_creation( grammar, test_num, result ):
#    """Tests the creation ofa dictionary of rules"""
