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
        S -> LESS_THAN HTML_NAME GREATER_THAN HTML_CONTENT LESS_THAN SLASH HTML_NAME GREATER_THAN | LESS_THAN HTML_NAME GREATER_THAN LESS_THAN SLASH HTML_NAME GREATER_THAN
        LESS_THAN -> '<'
        GREATER_THAN -> '>'
        SLASH -> '/'
        HTML_NAME -> 'html'
        HTML_CONTENT -> HEAD BODY | BODY

        HEAD -> LESS_THAN HEAD_NAME GREATER_THAN TITLE LESS_THAN SLASH HEAD_NAME GREATER_THAN
        HEAD_NAME -> 'head'

        TITLE -> LESS_THAN TITLE_NAME GREATER_THAN TEXT LESS_THAN SLASH TITLE_NAME GREATER_THAN
        TITLE_NAME -> 'title'
        
        BODY -> LESS_THAN BODY_NAME GREATER_THAN BODY_CONTENT LESS_THAN SLASH BODY_NAME GREATER_THAN
        BODY_CONTENT -> TEXT BODY_CONTENT | HEADING BODY_CONTENT | PARAGRAPH BODY_CONTENT | ANCHOR BODY_CONTENT | IMAGE BODY_CONTENT
        BODY_CONTENT -> LINE_BREAK BODY_CONTENT | HORIZONTAL_RULE BODY_CONTENT | INPUT BODY_CONTENT | STRONG BODY_CONTENT
        BODY_CONTENT -> TEXT | HEADING | PARAGRAPH | ANCHOR | IMAGE | LINE_BREAK | HORIZONTAL_RULE | INPUT | STRONG
        BODY_NAME -> 'body'

        HEADING -> H1 | H2 | H3 | H4 | H5 | H6

        INPUT -> LESS_THAN INPUT_NAME GREATER_THAN
        INPUT_NAME -> 'input'

        H1 -> LESS_THAN H1_NAME GREATER_THAN TEXT_NESTING LESS_THAN SLASH H1_NAME GREATER_THAN
        H2 -> LESS_THAN H2_NAME GREATER_THAN TEXT_NESTING LESS_THAN SLASH H2_NAME GREATER_THAN
        H3 -> LESS_THAN H3_NAME GREATER_THAN TEXT_NESTING LESS_THAN SLASH H3_NAME GREATER_THAN
        H4 -> LESS_THAN H4_NAME GREATER_THAN TEXT_NESTING LESS_THAN SLASH H4_NAME GREATER_THAN
        H5 -> LESS_THAN H5_NAME GREATER_THAN TEXT_NESTING LESS_THAN SLASH H5_NAME GREATER_THAN
        H6 -> LESS_THAN H6_NAME GREATER_THAN TEXT_NESTING LESS_THAN SLASH H6_NAME GREATER_THAN
        H1_NAME -> 'h1'
        H2_NAME -> 'h2'
        H3_NAME -> 'h3'
        H4_NAME -> 'h4'
        H5_NAME -> 'h5'
        H6_NAME -> 'h6'

        TEXT_NESTING -> TEXT TEXT_NESTING | INLINE_ELEMENTS TEXT_NESTING
        TEXT_NESTING -> TEXT | INLINE_ELEMENTS

        INLINE_ELEMENTS -> ANCHOR | IMAGE | LINE_BREAK | STRONG

        PARAGRAPH -> LESS_THAN PARAGRAPH_NAME GREATER_THAN TEXT_NESTING LESS_THAN SLASH PARAGRAPH_NAME GREATER_THAN
        PARAGRAPH_NAME -> 'p'

        ANCHOR -> LESS_THAN ANCHOR_NAME GREATER_THAN TEXT_NESTING LESS_THAN SLASH ANCHOR_NAME GREATER_THAN
        ANCHOR_NAME -> 'a'

        STRONG -> LESS_THAN STRONG_NAME GREATER_THAN TEXT_NESTING LESS_THAN SLASH STRONG_NAME GREATER_THAN
        STRONG_NAME -> 'strong'

        IMAGE -> LESS_THAN IMAGE_NAME GREATER_THAN
        IMAGE_NAME -> 'img'

        LINE_BREAK -> LESS_THAN LINE_BREAK_NAME GREATER_THAN
        LINE_BREAK_NAME -> 'br'

        HORIZONTAL_RULE -> LESS_THAN HORIZONTAL_RULE_NAME GREATER_THAN 
        HORIZONTAL_RULE_NAME -> 'hr'

        TEXT -> LETTERS TEXT | NUMBERS TEXT | LETTERS | NUMBERS
        LETTERS -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
        LETTERS -> 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z'
        NUMBERS -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

        
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