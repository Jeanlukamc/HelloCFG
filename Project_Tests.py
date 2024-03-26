#Tests
#By: Jean Luka Molina
#25/03/2024

import pytest
from CYK_Parser import test_valid_CFG
from Grammars import xml


@pytest.fixture
def grammar( ):
    return ( xml )

def test_is_valid_CFG( grammar ):
    """Test the validity of the grammar"""
    assert( test_valid_CFG( grammar ) == True )
    for item in grammar.productions( ):
        print( item )
    print( "Grammar is Accepted | PASSED")
