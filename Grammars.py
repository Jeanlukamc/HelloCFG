#Project #2
#By Jean Luka Molina Campos
#25/03/2024

from nltk import CFG

xml = CFG.fromstring(
    """
        S -> CONTEXT | LESS_THAN CONTEXT GREATER_THAN S LESS_THAN SLASH CONTEXT GREATER_THAN | LESS_THAN CONTEXT GREATER_THAN LESS_THAN SLASH CONTEXT GREATER_THAN
        S -> LESS_THAN EXCLAMATION DASH DASH CONTEXT DASH DASH GREATER_THAN
        S -> S LESS_THAN EXCLAMATION DASH DASH CONTEXT DASH DASH GREATER_THAN
        S -> LESS_THAN EXCLAMATION DASH DASH CONTEXT DASH DASH GREATER_THAN S
        LESS_THAN -> "<"
        GREATER_THAN -> ">"
        SLASH -> "/"
        EXCLAMATION -> '!'
        DASH -> '-'
        CONTEXT -> LETTER CONTEXT | SPACE CONTEXT | NUMBER CONTEXT | LETTER | SPACE | NUMBER
        LETTER -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
        NUMBER -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
        SPACE -> ' '
""")

alphabet_numbers = CFG.fromstring(
    """
        S -> LETTER S | NUMBER S | SPACE S | LETTER | NUMBER | SPACE
        LETTER -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
        NUMBER -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
        SPACE -> ' '
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