#Project #2
#By Jean Luka Molina Campos
#25/03/2024

from nltk import CFG

xml = CFG.fromstring(
    """
        S -> TEXT | LESS_THAN TAG GREATER_THAN S LESS_THAN SLASH TAG GREATER_THAN | LESS_THAN TAG GREATER_THAN LESS_THAN SLASH TAG GREATER_THAN
        S -> LESS_THAN EXCLAMATION DASH DASH TEXT DASH DASH GREATER_THAN
        S -> S LESS_THAN EXCLAMATION DASH DASH TEXT DASH DASH GREATER_THAN
        S -> LESS_THAN EXCLAMATION DASH DASH TEXT DASH DASH GREATER_THAN S
        S -> LESS_THAN TAG SPACE MULTI_ATTRIBUTES GREATER_THAN S LESS_THAN SLASH TAG GREATER_THAN | LESS_THAN TAG SPACE MULTI_ATTRIBUTES GREATER_THAN LESS_THAN SLASH TAG GREATER_THAN
        MULTI_ATTRIBUTES -> ATTRIBUTE SPACE MULTI_ATTRIBUTES | ATTRIBUTE
        ATTRIBUTE -> TAG EQUALS QUOTE TEXT QUOTE
        LESS_THAN -> "<"
        GREATER_THAN -> ">"
        SLASH -> "/"
        EXCLAMATION -> '!'
        DASH -> '-'
        AND_SYMBOL -> '&'
        SEMICOLON -> ';'
        EQUALS -> '='
        QUOTE -> '"'
        L_SYMBOL -> 'l'
        T_SYMBOL -> 't'
        A_SYMBOL -> 'a'
        M_SYMBOL -> 'm'
        P_SYMBOL -> 'p'
        O_SYMBOL -> 'o'
        S_SYMBOL -> 's'
        Q_SYMBOL -> 'q'
        U_SYMBOL -> 'u'
        G_SYMBOL -> 'g'
        TAG -> LETTERS TAG | LETTERS
        TEXT -> LETTERS TEXT | SPACE TEXT | NUMBER TEXT | ENTITY TEXT | LETTERS | SPACE | NUMBER | ENTITY
        ENTITY -> LT_SEMICOLON | GT_SEMICOLON | AMPERSAND | APOSTROPHE | QUOTATION_MARK
        LT_SEMICOLON -> AND_SYMBOL L_SYMBOL T_SYMBOL SEMICOLON
        GT_SEMICOLON -> AND_SYMBOL G_SYMBOL T_SYMBOL SEMICOLON
        AMPERSAND -> AND_SYMBOL A_SYMBOL M_SYMBOL P_SYMBOL SEMICOLON
        APOSTROPHE -> AND_SYMBOL A_SYMBOL P_SYMBOL O_SYMBOL S_SYMBOL SEMICOLON
        QUOTATION_MARK -> AND_SYMBOL Q_SYMBOL U_SYMBOL O_SYMBOL T_SYMBOL SEMICOLON
        LETTERS -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
        LETTERS -> 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z'
        NUMBER -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
        SPACE -> ' '
""")

html = CFG.fromstring(
    """
        S -> NP VP
        NP -> Det N
        VP -> V NP
        Det -> 'the' | 'a'
        N -> 'dog' | 'cat'
        V -> 'chases' | 'sees'
""")

invalid_CNF_grammar = CFG.fromstring(
    """
        S -> CONTEXT | LESS_THAN CONTEXT GREATER_THAN S SLASH_LESS_THAN CONTEXT GREATER_THAN | LESS_THAN CONTEXT GREATER_THAN SLASH_LESS_THAN CONTEXT GREATER_THAN
        LESS_THAN -> "<"
        GREATER_THAN -> ">"
        SLASH_LESS_THAN -> "</"
        CONTEXT -> LETTER CONTEXT | SPACE CONTEXT | NUMBER CONTEXT | ''
        LETTER -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
        NUMBER -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
        SPACE -> ' ' | ' ' B
""")

basic_grammar = CFG.fromstring(
    """
        S -> NP VP
        NP -> Det N
        VP -> V NP
        Det -> 'the' | 'a'
        N -> 'dog' | 'cat'
        V -> 'chases' | 'sees'
""")