#Tests
#By: Jean Luka Molina
#25/03/2024

import pytest
from CYK_Parser import valid_CFG, conversion_to_CNF
from Grammars import xml, invalid_CNF_grammar


@pytest.mark.parametrize( "grammar, result", [ ( xml, True ), (invalid_CNF_grammar, True) ] )
def test_valid_CFG( grammar, result):
    """Test the validity of the grammar"""
    assert( valid_CFG( grammar ) == result )
    for item in grammar.productions( ):
        print( item )
    print( "Grammar is Accepted | PASSED")
    print( "----------------------------------------------------------------------------------------------------\n" )

@pytest.mark.parametrize( "grammar, test_num, result", [ ( xml, 1, True ), (invalid_CNF_grammar, 2, False) ] )
def test_CNF_conversion( grammar, test_num, result ):
    """Tests whether a CFG can be turned into a CNF"""
    assert( conversion_to_CNF( grammar ) == result )
    if ( result ):
        for item in grammar.productions( ):
            print( item )
    print( f"Languege #{test_num} Result: {result} | PASSED")
    print( "----------------------------------------------------------------------------------------------------\n" )
