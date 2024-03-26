#Project #2
#By Jean Luka Molina Campos
#25/03/2024

from nltk import CFG
from pprint import pprint


def valid_CFG( grammar ):
    """Tests whether a grammar is Context Free"""

    list_test = grammar.productions( )

    if ( len( list_test ) != 0 ):
        return( True )
    else:
        return( False )
    
def conversion_to_CNF( grammar ):
    """Tries to convert the Context Free Grammar into Chomsky Normal Form"""
    try:
        #Validate that it's a valid CFG first of all
        if( valid_CFG( grammar ) == False ):
            return( False )
        
        CNF_grammar = grammar.chomsky_normal_form( )

        return( True )
    except Exception as e:
        print( f"An unexpected error occurred: {e}" )
        return ( False )


def dictionary_creation( grammar_rules ):
    """Creates a dictionary for the """
    rule_dict = {}

    for production in grammar_rules:
        left_hand_side = str( production.lhs( ) )

        symbols = production.rhs( )
        symbol_strings = []

        for symbol in symbols:
            symbol_strings.append( str( symbol ) )

        right_hand_side = tuple( symbol_strings )

        if left_hand_side in rule_dict:
            rule_dict[ left_hand_side ].append( right_hand_side )
        else:
            rule_dict[left_hand_side] = [ right_hand_side ]
    #pprint( rule_dict )
    return ( rule_dict )

def cyk_parser( rule_dictionary, string ):
    """Does the CYK algorithm based on a dictionary of rules"""
