#Morse Code
#By: Jean Luka Molina
#30/03/2020

MORSE_CODE_DICT = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
                   '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
                   '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
                   '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                   '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
                   '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
                   '....-': '4', '.....': '5', '-....': '6', '--...': '7',
                   '---..': '8', '----.': '9', '-----': '0', '--..--': ', ',
                   '.-.-.-': '.', '..--..': '?', '-....-': '-',
                   '-.--.': '(', '-.--.-': ')', '/': ' '}

def english_equivalent( morse_code ):
    """Gives the equivalent """
    words = morse_code.split( '/' ) #/ represents a separation between words
    message = ""

    for word in words:
        letters = word.split( '#' ) #1 space means separation between letters
        for letter in letters:
            if letter in MORSE_CODE_DICT:
                message += MORSE_CODE_DICT[ letter ]
            else:
                message += "<INVALID>"
        message += " "
    message = message.strip( )
    return( message )

def main( ):
    """Controls previous functions"""
    morse = input ( "Write a sentence you would like to be translated: " )
    #morse = "....#.#.-..#.-..#---/.--#---#.-.#.-..#-.."
    english = english_equivalent( morse )
    print ( english )

main( )