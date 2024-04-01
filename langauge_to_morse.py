#Morse Code
#By: Jean Luka Molina
#30/03/2020

from morse_to_language import morse_english_input_collector, english_equivalent
from CYK_Parser import dictionary_creation, cyk_parser
from Grammars import morse_grammar

LANGUAGE_TO_MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '0': '-----', ' ': '/', '<' : '<',
}
ENDING_SYMBOLS = [ '>', '(', ')', ':', '"', "_", ',', '{', '}' ]

"""
RESERVED LIST BY INDEX:
- <WHILE>
- <FOR>
- <IN>
- <RANGE>
- <IF>
- <ELSE>
- <ADD>
- <SUB>
- <MULT>
- <DIV>
- <MOD>
- <RETURN>
- <SWITCH>
- <EQUALS>
- <POWER>
- <CONST>
- <PRINT>
- <DEF>
- <LESS>
- <GREATER>
"""
RESERVED_MORSE = [ 
    '<#.--#....#..#.-..#.#>#', '<#..-.#---#.-.#>#', '<#..#-.#>#', '<#.-.#.-#-.#--.#.#>#', '<#..#..-.#>#',
    '<#.#.-..#...#.#>#', '<#.-#-..#-..#>#', '<#...#..-#-...#>#',
    '<#--#..-#.-..#-#>#', '<#-..#..#...-#>#', '<#--#---#-..#>#', '<#.-.#.#-#..-#.-.#-.#>#',
    '<#...#.--#..#-#-.-.#....#>#', '<#.#--.-#..-#.-#.-..#...#>#', '<#.--.#---#.--#.#.-.#>#',
    '<#-.-.#---#-.#...#-#>#', '<#.--.#.-.#..#-.#-#>#', '<#-..#.#..-.#>#', '<#.-..#.#...#...#>#', '<#--.#.-.#.#.-#-#.#.-.#>#' 
]

def morse_code_equivalent ( sentence ):
    """Will give the morse code equivalent of the input string"""
    words = sentence.split( " " )

    morse_code_words = []
    current_word = ""
    #Go through every word
    for word in words:
        #Go through every letter in the word
        for letter in word:
            #If valid, add to the current word its morse equivalent
            if ( letter in LANGUAGE_TO_MORSE_DICT ):
                current_word += LANGUAGE_TO_MORSE_DICT[ letter ] + '#'
            #If it's an exception, then add it with a space to separate it later on
            elif( letter in ENDING_SYMBOLS ):
                current_word += ENDING_SYMBOLS[ ENDING_SYMBOLS.index( letter ) ] + '#/'
            else:
                current_word += "<INVALID>"
        morse_code_words.append( current_word )
        morse_code_words.append( '/' )
        current_word = ""
    morse_sentence = "".join(morse_code_words)
    return morse_sentence

def morse_tokenizer( string ):
    """Tokenizes properly the string that we have"""
    tokens = string.split( '/' )
    if( '' in tokens ):
        tokens.remove( '' )
    #print( f"BEFORE TOKENS: {tokens}" )

    new_tokens = []
    for item in tokens:
        #If the item is part of the Reserved Morse
        if ( item in RESERVED_MORSE ):
            #print(f"FOUND: {item}")
            new_tokens.append( item )
        else:
            morse_token = ""
            for letter in item:
                if ( letter !=  '#' ):
                    morse_token += letter
                else:
                    morse_token += letter
                    new_tokens.append( morse_token )
                    morse_token = ""
    
    print( f"TOKENS: {new_tokens}" )
    return( new_tokens )


def edit_morse_file_equivalent( file_name, morse_string ):
    """Creates/Edits a file to be the morse code equivalent of it"""
    with open( file_name, "w" ) as file:
        file.write( morse_string )
    
    file.close( )

cnf_morse_dict = dictionary_creation( morse_grammar.chomsky_normal_form( ).productions( ) )
file_number = 6
file_1 = "FILES\\Morse_Code_Files\\english_" + str( file_number) + ".txt"
file_2 = "FILES\\Morse_Code_Files\\morse_" + str( file_number) + ".txt"

my_input = morse_english_input_collector( file_1 )
print( f"My Input: {my_input}")
morse =  morse_code_equivalent( my_input )
edit_morse_file_equivalent( file_2, morse )

my_input = morse_english_input_collector( file_2 )
tokens = morse_tokenizer( my_input )

#print( cyk_parser( cnf_morse_dict, tokens ) )

print( f"MORSE: {morse}" )
print( f"ENGLISH: {english_equivalent( morse )}")
#main( )
