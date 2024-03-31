#Morse Code
#By: Jean Luka Molina
#30/03/2020

MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9', '-----': '0', '/': ' ',
    '<': '<', '>' : '>'
    }

EXCEPTIONS = [ '<', '>', '(', ')', ':' ]

def english_equivalent( morse_code ):
    """Gives the equivalent """
    words = morse_code.strip( '/' ).split( '/' )
    message = ""

    for word in words:
        letters = word.split( '#' )
        letters = letters[:-1]
        for letter in letters:
            if ( letter in MORSE_CODE_DICT ):
                message += MORSE_CODE_DICT[ letter ]
            elif ( letter in EXCEPTIONS ):
                message += letter
            else:
                message += "<INVALID>"
        message += " "
    message = message.strip( )
    return( message )

def morse_english_input_collector( input_file ):
    """Collects the input from the file"""
    result = ""

    with open( input_file ) as file:
        for line in file:
            line = line.strip( ).replace( '\n', '')
            result = result + line + ' '
    result = result.strip( )

    return( result.upper( ) )