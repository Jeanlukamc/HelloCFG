#Project #2
#By Jean Luka Molina Campos
#25/03/2024

from nltk import CFG
from Grammars import html

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
    

def input_collector( input_file ):
    """Collects the input from the file"""
    result = ""

    with open( input_file ) as file:
        for line in file:
            result = result + line.strip( )
    return( result )

def html_input_tokenizer( file_input ):
    """Tokenizes the input in the context for html and xml"""
    lookout_chars = ["<", ">", "/"]

    tokens = []
    current_token = ""
    inside_tag = False

    for char in file_input:
        if ( char in lookout_chars ):
            if ( current_token != "" ):
                if ( not inside_tag ):
                    tokens += process_text_tokens( current_token )
                else:

                    tokens += current_token.split( )
            
                current_token = ""
            tokens.append( char )

            if ( char == "<" ):
                inside_tag = True
            elif ( char == ">" ):
                inside_tag = False
        else:
            current_token += char
    
    if ( current_token != "" ):
        if ( not inside_tag ):
            tokens += process_text_tokens( current_token )
        else:
            tokens.append( current_token )
    
    print( f"Tokens Taken: {tokens}" )
    return( tokens )


def process_text_tokens( token ):
    """Trim text tokens to individual characters, excluding whitespace"""
    
    text_tokens = []
    for char in token:
        if ( char != " " ):
            text_tokens.append( char )
    return( text_tokens )



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
    return ( rule_dict )

def cyk_parser( rule_dictionary, string ):
    """Does the CYK algorithm based on a dictionary of rules"""

    letter_count = len( string )

    #Create the table based on the size of symbols/words we're going to use
    table = [ [ set( ) for _ in range( letter_count ) ] for _ in range( letter_count ) ]

    #Fill the table 
    for i, letter in enumerate( string ):
        for left_hand_side, right_hand_side in rule_dictionary.items( ):
            #If the letter is part of the RHS, add the LHS to the corresponding cell in the table
            if (letter,) in right_hand_side:
                table[ i ][ i ].add( left_hand_side )
    
    #Fill the table with substrings/symbols by combining smaller substrings/other symbols that have been processed
    for length in range( 2, letter_count + 1 ):
        for i in range( letter_count - length + 1 ):
            for j in range( i + 1, i + length ):
                #Trying to combine substrings/symbols
                for k in range( i, j ):
                    #Check production rules
                    for left_hand_side, rhs_list in rule_dictionary.items( ):
                        for right_hand_side in rhs_list:
                            #Check for binary productions
                            if len( right_hand_side ) == 2:
                                B, C = right_hand_side
                                #If B can generate the first part of the substring and C can generate
                                #the second part, then A (lhs) can generate the entire substring.
                                if ( B in table[ i ][ k ] and C in table[ k + 1 ][ i + length - 1] ):
                                    table[ i ][ i + length - 1 ].add( left_hand_side )
    
    #Return Tre or False depending if 'S' is in the top-right cell of the table
    return( 'S' in table[ 0 ][ letter_count - 1] )

#test = input_collector( "FILES\\HTML_Files\\HTML_8.txt" )

#tokens = html_input_tokenizer( test )

#cnf_html_dict = dictionary_creation( html.chomsky_normal_form( ).productions( ) )
#print( cyk_parser( cnf_html_dict, tokens ) )