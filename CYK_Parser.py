#Project #2
#By Jean Luka Molina Campos
#25/03/2024

from nltk import CFG
from pprint import pprint
from Grammars import xml, basic_grammar, alphabet_numbers


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
    """Creates a dictionary for the CYK algorithm to process"""
    rule_dict = {}

    for production in grammar_rules:
        left_hand_side = str( production.lhs( ) )

        right_hand_side = tuple(str(symbol) for symbol in production.rhs())

        if left_hand_side not in rule_dict:
            rule_dict[left_hand_side] = set()
        
        # Add the RHS as a tuple of strings to the set for the corresponding LHS
        rule_dict[left_hand_side].add(right_hand_side)
    pprint( rule_dict )
            
    #for production in grammar_rules:
    #    print( f"LHS: {production.lhs( )} | RHS: {production.rhs( )}")
    return ( rule_dict )

def cyk_parser( rule_dictionary, words ):
    """Does the CYK algorithm based on a dictionary of rules"""

    word_count = len( words )

    table = [ [ set( ) for _ in range( word_count ) ] for _ in range( word_count ) ]

    for i, word in enumerate( words ):
        for left_hand_side, right_hand_side in rule_dictionary.items( ):
            if (word,) in right_hand_side:
                table[ i ][ i ].add( left_hand_side )
    
    for length in range( 2, word_count + 1 ):
        for i in range( word_count - length + 1 ):
            for j in range( i + 1, i + length ):
                for k in range( i, j ):
                    for left_hand_side, rhs_list in rule_dictionary.items( ):
                        for right_hand_side in rhs_list:
                            if len( right_hand_side ) == 2:
                                B, C = right_hand_side
                                if ( B in table[ i ][ k ] and C in table[ k + 1 ][ i + length - 1] ):
                                    table[ i ][ i + length - 1 ].add( left_hand_side )
    
    return( 'S' in table[ 0 ][ word_count - 1] )

my_dict = dictionary_creation( xml.chomsky_normal_form( ).productions( ) )
#pprint(my_dict)

string1 = "the dog sees a cat"
string2 = "the cat chases the dog"
string3 = "dog chases cat"
string4 = "chases the dog the cat"
words = string1.split()

letters = list( "<b><d> hello world</bbb></b>" )


print( cyk_parser(my_dict, letters ) )