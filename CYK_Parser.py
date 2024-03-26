#Project #2
#By Jean Luka Molina Campos
#25/03/2024

from nltk import CFG


def test_valid_CFG( grammar ):
    """Tests whether a grammar is Context Free"""

    list_test = grammar.productions( )

    if ( len( list_test ) != 0 ):
        return( True )
    else:
        return( False )
