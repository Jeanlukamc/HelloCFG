#Project #2
#By Jean Luka Molina Campos
#25/03/2024

from nltk import CFG

xml = CFG.fromstring(
    """
        SOURCE -> CONTEXT | LESS_THAN CONTEXT GREATER_THAN SOURCE SLASH_LESS_THAN CONTEXT GREATER_THAN | LESS_THAN CONTEXT GREATER_THAN SLASH_LESS_THAN CONTEXT GREATER_THAN
        LESS_THAN -> "<"
        GREATER_THAN -> ">"
        SLASH_LESS_THAN -> "</"
        CONTEXT -> LETTER CONTEXT | SPACE CONTEXT | NUMBER CONTEXT | ''
        LETTER -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
        NUMBER -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
        SPACE -> ' '
""")

invalid_CNF_grammar = CFG.fromstring(
    """
        SOURCE -> CONTEXT | LESS_THAN CONTEXT GREATER_THAN SOURCE SLASH_LESS_THAN CONTEXT GREATER_THAN | LESS_THAN CONTEXT GREATER_THAN SLASH_LESS_THAN CONTEXT GREATER_THAN
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
        PP -> P NP
        NP -> Det N | NP PP
        VP -> V NP | VP PP VP
        Det -> 'a' | 'the'
        N -> 'dog' | 'cat'
        V -> 'chased' | 'sat'
        P -> 'on' | 'in'
""")

#c = basic_grammar.chomsky_normal_form( ).productions( )
#print( c )
#for production in c:
#    print( f"Left Hand Side: {production.lhs( )} | Right Hand Side: {production.rhs( )}" )