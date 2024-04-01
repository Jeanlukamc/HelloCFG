#Project #2
#By Jean Luka Molina Campos
#25/03/2024

from nltk import CFG


morse_grammar = CFG.fromstring(
    """
    S -> EXPRESSION S | COMPARISON S | ASSIGNMENT S | CONSTANT S | PRINT S | IF_STATEMENT S | FOR_LOOP S
    S -> EXPRESSION | COMPARISON | ASSIGNMENT | CONSTANT | PRINT | IF_STATEMENT | FOR_LOOP
    
    FOR_LOOP -> FOR_LOOP_NAME VARIABLE IN_NAME SEQUENCE COLON OPEN_CURLY_BRACKET S CLOSE_CURLY_BRACKET
    SEQUENCE -> VARIABLE | STRING | RANGE
    RANGE -> RANGE_NAME OPEN_PARENTHESIS RANGE_CONTENT CLOSE_PARENTHESIS
    RANGE_CONTENT -> DIGITS COMMA DIGITS | DIGITS COMMA DIGITS COMMA DIGITS
    FOR_LOOP_NAME -> '<#..-.#---#.-.#>#'
    IN_NAME -> '<#..#-.#>#'
    RANGE_NAME -> '<#.-.#.-#-.#--.#.#>#'

    IF_STATEMENT -> IF_STATEMENT_NAME OPEN_PARENTHESIS COMPARISON CLOSE_PARENTHESIS COLON OPEN_CURLY_BRACKET S CLOSE_CURLY_BRACKET
    IF_STATEMENT -> IF_STATEMENT_NAME COMPARISON COLON OPEN_CURLY_BRACKET S CLOSE_CURLY_BRACKET 
    IF_STATEMENT -> IF_STATEMENT_NAME OPEN_PARENTHESIS COMPARISON CLOSE_PARENTHESIS COLON OPEN_CURLY_BRACKET S CLOSE_CURLY_BRACKET ELSE_STATEMENT_NAME COLON OPEN_CURLY_BRACKET S CLOSE_CURLY_BRACKET
    IF_STATEMENT -> IF_STATEMENT_NAME COMPARISON COLON OPEN_CURLY_BRACKET S CLOSE_CURLY_BRACKET ELSE_STATEMENT_NAME COLON OPEN_CURLY_BRACKET S CLOSE_CURLY_BRACKET
    IF_STATEMENT_NAME -> '<#..#..-.#>#'
    ELSE_STATEMENT_NAME -> '<#.#.-..#...#.#>#'

    PRINT -> PRINT_NAME OPEN_PARENTHESIS EXPRESSION CLOSE_PARENTHESIS
    PRINT_NAME -> '<#.--.#.-.#..#-.#-#>#'

    CONSTANT -> CONSTANT_NAME VARIABLE EQUALS STRING | CONSTANT_NAME VARIABLE EQUALS DIGITS
    CONSTANT_NAME -> '<#-.-.#---#-.#...#-#>#'

    ASSIGNMENT -> VARIABLE EQUALS EXPRESSION
    EQUALS -> '<#.#--.-#..-#.-#.-..#...#>#'

    COMPARISON -> EXPRESSION EQUALS EQUALS EXPRESSION

    EXPRESSION -> EXPRESSION ADDITION TERM | EXPRESSION SUBTRACTION TERM | TERM
    TERM -> TERM MULTIPLICATION FACTOR | TERM DIVISION FACTOR | TERM MOD FACTOR | FACTOR
    FACTOR -> OPEN_PARENTHESIS EXPRESSION CLOSE_PARENTHESIS | FACTOR POWER FACTOR | VARIABLE | STRING | DIGITS

    OPEN_PARENTHESIS -> '(#'
    CLOSE_PARENTHESIS -> ')#'
    OPEN_CURLY_BRACKET -> '{#'
    CLOSE_CURLY_BRACKET -> '}#'
    UNDERSCORE -> '_#'
    QUOTE -> '"#'
    COLON -> ':#'
    COMMA -> ',#'
    ADDITION -> '<#.-#-..#-..#>#'
    SUBTRACTION -> '<#...#..-#-...#>#'
    MULTIPLICATION -> '<#--#..-#.-..#-#>#'
    MOD -> '<#--#---#-..#>#'
    DIVISION -> '<#-..#..#...-#>#'
    POWER -> '<#.--.#---#.--#.#.-.#>#'


    VARIABLE -> TEXT_START
    TEXT_START -> LETTERS TEXT_END | UNDERSCORE TEXT_END | LETTERS | UNDERSCORE
    TEXT_END -> LETTERS TEXT_END | DIGITS TEXT_END | UNDERSCORE TEXT_END | LETTERS | DIGITS | UNDERSCORE

    STRING -> QUOTE STRING_CONTENT QUOTE
    STRING_CONTENT -> LETTERS STRING_CONTENT | NUMBERS STRING_CONTENT | SPECIAL_CHARACTERS STRING_CONTENT
    STRING_CONTENT -> LETTERS | NUMBERS | SPECIAL_CHARACTERS
    
    DIGITS -> NUMBERS DIGITS | NUMBERS
    
    SPECIAL_CHARACTERS -> OPEN_PARENTHESIS | CLOSE_PARENTHESIS | UNDERSCORE
    LETTERS -> '.-#' | '-...#' | '-.-.#' | '-..#' | '.#' | '..-.#' | '--.#' | '....#' | '..#' | '.---#' | '-.-#' | '.-..#' | '--#' | '-.#' | '---#' | '.--.#' | '--.-#' | '.-.#' | '...#' | '-#' | '..-#' | '...-#' | '.--#' | '-..-#' | '-.--#' | '--..#'
    NUMBERS -> '-----#' | '.----#' | '..---#' | '...--#' | '....-#' | '.....#' | '-....#' | '--...#' | '---..#' | '----.#'


""")

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
        S -> LESS_THAN HTML_NAME  GLOBAL_ATTRIBUTES GREATER_THAN HTML_CONTENT LESS_THAN SLASH HTML_NAME GREATER_THAN | LESS_THAN HTML_NAME GLOBAL_ATTRIBUTES GREATER_THAN LESS_THAN SLASH HTML_NAME GREATER_THAN
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
        BODY_CONTENT -> LINE_BREAK BODY_CONTENT | HORIZONTAL_RULE BODY_CONTENT | INPUT BODY_CONTENT | STRONG BODY_CONTENT | SPAN BODY_CONTENT
        BODY_CONTENT -> EMPHASIS BODY_CONTENT | UNORDERED_LIST BODY_CONTENT | ORDERED_LIST BODY_CONTENT | DIVISION BODY_CONTENT
        BODY_CONTENT -> FORM BODY_CONTENT | TEXT_AREA BODY_CONTENT
        BODY_CONTENT -> TEXT | HEADING | PARAGRAPH | ANCHOR | IMAGE | LINE_BREAK | HORIZONTAL_RULE | INPUT | STRONG | SPAN | EMPHASIS
        BODY_CONTENT -> UNORDERED_LIST | ORDERED_LIST | DIVISION | FORM | TEXT_AREA
        BODY_NAME -> 'body'

        GLOBAL_ATTRIBUTES -> GLOBAL_ATTRIBUTE GLOBAL_ATTRIBUTES | GLOBAL_ATTRIBUTE
        GLOBAL_ATTRIBUTE -> LANG_ATTRIBUTE | DIRECTORY_ATTRIBUTE
        LANG_ATTRIBUTE -> LANG_ATTRIBUTE_NAME TEXT QUOTE
        LANG_ATTRIBUTE_NAME -> 'lang="'
        DIRECTORY_ATTRIBUTE -> DIRECTORY_ATTRIBUTE_NAME TEXT QUOTE
        DIRECTORY_ATTRIBUTE_NAME -> 'dir="'

        FORM -> LESS_THAN FORM_NAME GREATER_THAN FORM_CONTENT LESS_THAN SLASH FORM_NAME GREATER_THAN
        FORM -> LESS_THAN FORM_NAME FORM_ATTRIBUTES GREATER_THAN FORM_CONTENT LESS_THAN SLASH FORM_NAME GREATER_THAN
        FORM_CONTENT -> INPUT FORM_CONTENT | TEXT_AREA FORM_CONTENT
        FORM_CONTENT -> INPUT | TEXT_AREA
        FORM_ATTRIBUTES -> ACTION_ATTRIBUTE GLOBAL_ATTRIBUTES
        FORM_ATTRIBUTES -> ACTION_ATTRIBUTE | GLOBAL_ATTRIBUTES
        ACTION_ATTRIBUTE -> ACTION_ATTRIBUTE_NAME TEXT QUOTE
        ACTION_ATTRIBUTE_NAME -> 'action="'
        FORM_NAME -> 'form'

        TEXT_AREA -> LESS_THAN TEXT_AREA_NAME  TEXT_AREA_ATTRIBUTES GREATER_THAN TEXT LESS_THAN SLASH TEXT_AREA_NAME GREATER_THAN
        TEXT_AREA_ATTRIBUTES -> ID_ATTRIBUTE TEXT_AREA_ATTRIBUTES | NAME_ATTRIBUTE TEXT_AREA_ATTRIBUTES | ROWS_ATTRIBUTE TEXT_AREA_ATTRIBUTES
        TEXT_AREA_ATTRIBUTES -> COLUMNS_ATTRIBUTE TEXT_AREA_ATTRIBUTES | GLOBAL_ATTRIBUTES TEXT_AREA_ATTRIBUTES
        TEXT_AREA_ATTRIBUTES -> ID_ATTRIBUTE | NAME_ATTRIBUTE | ROWS_ATTRIBUTE | COLUMNS_ATTRIBUTE | GLOBAL_ATTRIBUTES
        ID_ATTRIBUTE -> ID_ATTRIBUTE_NAME TEXT QUOTE
        ID_ATTRIBUTE_NAME -> 'id="'
        NAME_ATTRIBUTE -> NAME_ATTRIBUTE_NAME TEXT QUOTE
        NAME_ATTRIBUTE_NAME -> 'name="'
        ROWS_ATTRIBUTE -> ROWS_ATTRIBUTE_NAME TEXT QUOTE
        ROWS_ATTRIBUTE_NAME -> 'rows="'
        COLUMNS_ATTRIBUTE -> COLUMNS_ATTRIBUTE_NAME TEXT QUOTE
        COLUMNS_ATTRIBUTE_NAME -> 'cols="'
        TEXT_AREA_NAME -> 'textarea'

        DIVISION -> LESS_THAN DIVISION_NAME GREATER_THAN  DIV_CONTENT LESS_THAN SLASH DIVISION_NAME GREATER_THAN
        DIV_CONTENT -> BODY_CONTENT
        DIVISION_NAME -> 'div'

        UNORDERED_LIST -> LESS_THAN UNORDERED_LIST_NAME GREATER_THAN LIST_ITEMS LESS_THAN SLASH UNORDERED_LIST_NAME GREATER_THAN
        UNORDERED_LIST_NAME -> 'ul'
        ORDERED_LIST -> LESS_THAN ORDERED_LIST_NAME GREATER_THAN LIST_ITEMS LESS_THAN SLASH ORDERED_LIST_NAME GREATER_THAN
        ORDERED_LIST_NAME -> 'ol'

        LIST_ITEMS -> LIST_ITEM LIST_ITEMS | LIST_ITEM
        LIST_ITEM -> LESS_THAN LIST_ITEM_NAME GREATER_THAN LIST_ITEM_CONTENT LESS_THAN SLASH LIST_ITEM_NAME GREATER_THAN
        LIST_ITEM_NAME -> 'li'
        LIST_ITEM_CONTENT -> UNORDERED_LIST LIST_ITEM_CONTENT | ORDERED_LIST LIST_ITEM_CONTENT | TEXT_NESTING LIST_ITEM_CONTENT | DIVISION LIST_ITEM_CONTENT
        LIST_ITEM_CONTENT -> UNORDERED_LIST | ORDERED_LIST | TEXT_NESTING | DIVISION

        HEADING -> H1 | H2 | H3 | H4 | H5 | H6

        INPUT -> LESS_THAN INPUT_NAME INPUT_ATTRIBUTES GREATER_THAN
        INPUT_ATTRIBUTES -> TYPE_ATTRIBUTE GLOBAL_ATTRIBUTES | TYPE_ATTRIBUTE
        TYPE_ATTRIBUTE -> TYPE_ATTRIBUTE_NAME TEXT QUOTE
        TYPE_ATTRIBUTE_NAME -> 'type="'
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

        INLINE_ELEMENTS -> ANCHOR | IMAGE | LINE_BREAK | STRONG | SPAN | EMPHASIS

        PARAGRAPH -> LESS_THAN PARAGRAPH_NAME GREATER_THAN TEXT_NESTING LESS_THAN SLASH PARAGRAPH_NAME GREATER_THAN
        PARAGRAPH_NAME -> 'p'

        ANCHOR -> LESS_THAN ANCHOR_NAME GREATER_THAN TEXT_NESTING LESS_THAN SLASH ANCHOR_NAME GREATER_THAN
        ANCHOR -> LESS_THAN ANCHOR_NAME ANCHOR_ATTRIBUTES GREATER_THAN TEXT_NESTING LESS_THAN SLASH ANCHOR_NAME GREATER_THAN
        ANCHOR_ATTRIBUTES -> HYPERTEXT_ATTRIBUTE GLOBAL_ATTRIBUTES | HYPERTEXT_ATTRIBUTE
        HYPERTEXT_ATTRIBUTE -> HYPERTEXT_ATTRIBUTE_NAME TEXT QUOTE
        HYPERTEXT_ATTRIBUTE_NAME -> 'href="'
        ANCHOR_NAME -> 'a'

        STRONG -> LESS_THAN STRONG_NAME GREATER_THAN TEXT_NESTING LESS_THAN SLASH STRONG_NAME GREATER_THAN
        STRONG_NAME -> 'strong'

        SPAN -> LESS_THAN SPAN_NAME GREATER_THAN TEXT_NESTING LESS_THAN SLASH SPAN_NAME GREATER_THAN
        SPAN_NAME -> 'span'

        EMPHASIS -> LESS_THAN EMPHASIS_NAME GREATER_THAN TEXT_NESTING LESS_THAN SLASH EMPHASIS_NAME GREATER_THAN
        EMPHASIS_NAME -> 'em'

        IMAGE -> LESS_THAN IMAGE_NAME IMAGE_ATTRIBUTES GREATER_THAN
        IMAGE_ATTRIBUTES -> SOURCE_ATTRIBUTE ALT_ATTRIBUTE GLOBAL_ATTRIBUTES | SOURCE_ATTRIBUTE ALT_ATTRIBUTE
        SOURCE_ATTRIBUTE -> SOURCE_ATTRIBUTE_NAME TEXT QUOTE
        SOURCE_ATTRIBUTE_NAME -> 'src="'
        ALT_ATTRIBUTE -> ALT_ATTRIBUTE_NAME TEXT QUOTE
        ALT_ATTRIBUTE_NAME -> 'alt="'
        IMAGE_NAME -> 'img'

        LINE_BREAK -> LESS_THAN LINE_BREAK_NAME GREATER_THAN
        LINE_BREAK_NAME -> 'br'

        HORIZONTAL_RULE -> LESS_THAN HORIZONTAL_RULE_NAME GREATER_THAN 
        HORIZONTAL_RULE_NAME -> 'hr'

        QUOTE -> '"'

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