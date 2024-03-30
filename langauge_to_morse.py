#Morse Code
#By: Jean Luka Molina
#30/03/2020

LANGUAGE_TO_MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '0': '-----', ' ': '@'
}

EXCEPTIONS = [ '=', '+', '-', '/', '*', '%', '(', ')' ]
EXCEPTIONS_DICT = {
    '=' : '<#.#--.-#..-#.-#.-..#...#>#', '+' : '<#.-#-..#-..#>#',
    '-' : '<#...#..-#-...#>#', '/' : '<#-..#..#...-#>#',
    '*' : '<#--#..-#.-..#-#>#', '%' : '<#--#---#-..#>#',
    '(' : '(#', ')' : ')#'
}


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
            elif ( letter in EXCEPTIONS ):
                current_word += EXCEPTIONS_DICT[ letter ]
            else:
                current_word += "<INVALID>"
        morse_code_words.append( current_word )
        morse_code_words.append( '@' )
        current_word = ""
        

                
    morse_sentence = "".join(morse_code_words)
    return morse_sentence

def main( ):
    """Controls previous functions"""
    sentence = input ("Write a sentence you would like to be translated: ")
    sentence = sentence.upper( )             #This counters every letter in lower case so its morse code equivalents will be appended.
    morse_code = morse_code_equivalent( sentence )
    print ( morse_code )

#main( )
