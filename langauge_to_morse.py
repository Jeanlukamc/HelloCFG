#Morse Code
#By: Jean Luka Molina
#30/03/2020

from morse_to_language import morse_input_collector, english_equivalent

LANGUAGE_TO_MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '0': '-----', ' ': '/',
    '<': '<', '>' : '>', '(' : '(', ')' : ')'
}

RESERVED_MORSE_DICT = [ ]


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
            else:
                current_word += "<INVALID>"
        morse_code_words.append( current_word )
        morse_code_words.append( '/' )
        current_word = ""
    morse_sentence = "".join(morse_code_words)
    return morse_sentence

def morse_tokenizer( tokens ):
    """Tokenizes properly the list of words that we have"""


def main( ):
    """Controls previous functions"""
    sentence = input ("Write a sentence you would like to be translated: ")
    sentence = sentence.upper( )             #This counters every letter in lower case so its morse code equivalents will be appended.
    morse_code = morse_code_equivalent( sentence )
    print ( morse_code )

my_input = morse_input_collector( "FILES\\Morse_Code_Files\\TEST.txt" ).upper( )
print( f"MY RESULT: {my_input}" )
morse =  morse_code_equivalent( my_input )
print( morse)
print( english_equivalent( morse ))
#main( )
