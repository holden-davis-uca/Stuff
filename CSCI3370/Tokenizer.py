#CSCI 3370 - CRN 22513
#Holden Davis - 10/27/21
#Dr. P - Fall 2021
#Jack Language Tokenizer Lab

#Define the group of all uppercase letters, lowercase letters, numbers and underscore characters that can be used to make an "identifier" in Jack syntax
identifiers = "_", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
#Define the reserved keywords in Jack syntax
keywords = "class", "constructor", "method", "function", "int", "boolean", "char", "void", "var", "static", "field", "let", "do", "if", "else", "while", "return", "true", "false", "null", "this"
#Define the symbols in Jack syntax
symbols = "(", ")", "[", "]", "{", "}", ",", ";", "=", ".", "+", "-", "*", "/", "&", "|", "~", "<", ">"
#Define integer constants in Jack syntax
intconstantnums = "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"

def run():
    #Write the header
    outfile.write("<tokens>\n")

    #Initialize and reset all helper variables
    sliteral = ""
    iliteral = ""
    symbol = ""
    thing = ""
    lex = 0

    #Iteratively proceed through the array and process characters until array is empty
    while lex < len(lexemes):
        #/
        if lexemes[lex] == "/":
            #Single line comment //, iterate and ignore everything until the end of the line
            if lexemes[lex+1] == "/":
                while lexemes[lex] != "\n":
                    lex = lex+1
            #Multiline /* */ or API /** */ commment, iterate and ignore everything until comment end sequence */
            elif lexemes[lex+1] == "*":
                while lexemes[lex-1] != "*" or lexemes[lex] != "/":
                    lex = lex + 1
            #Not a comment of any kind, simply a /
            else:
                symbol += lexemes[lex]
                outfile.write("<symbol> " + symbol + " </symbol>\n")
                symbol = ""
        #Quotes for string constant " "
        elif lexemes[lex] == '"':
            lex = lex + 1
            #Add all of the contents of the string constant together and write it out as such
            while lexemes[lex] != '"':
                sliteral += lexemes[lex]
                lex = lex+1
            outfile.write("<stringConstant> " + sliteral + " </stringConstant>\n")
            #Catches discarded character due to while loop behavior with iteration
            if lexemes[lex] in symbols:
                symbol += lexemes[lex]
                outfile.write("<symbol> " + symbol + " </symbol>\n")
                symbol = ""
            sliteral = ""
        #Integer for integer constant
        elif lexemes[lex] in intconstantnums:
            while lexemes[lex] in intconstantnums:
                iliteral += lexemes[lex]
                lex = lex + 1
            outfile.write("<integerConstant> " + iliteral + " </integerConstant>\n")
            #Catches discarded character due to while loop behavior with iteration
            if lexemes[lex] in symbols:
                symbol += lexemes[lex]
                outfile.write("<symbol> " + symbol + " </symbol>\n")
                symbol = ""
            iliteral = ""
        #Symbol
        elif lexemes[lex] in symbols:
            #Normally print symbols except the 4 symbols not permitted in XML
            symbol += lexemes[lex]
            if symbol == "<": symbol = "&lt;"
            if symbol == ">": symbol = "&gt;"
            if symbol == '"': symbol = "&quot;"
            if symbol == "&": symbol = "&amp;"
            outfile.write("<symbol> " + symbol + " </symbol>\n")
            symbol = ""
        #If its not in any of the other classes and its a _, number of letter, it must belong to an identifer or keyword
        elif lexemes[lex] in identifiers:
            while lexemes[lex] in intconstantnums or lexemes[lex] in identifiers:
                thing += lexemes[lex]
                lex = lex + 1
            #If the computed "word" is a keyword, write out as such
            if thing in keywords:
                outfile.write("<keyword> " + thing + " </keyword>\n")
            #Otherwise, write it out as an identifier
            else: outfile.write("<identifier> " + thing + " </identifier>\n")
            #Catches discarded character due to while loop behavior with iteration
            if lexemes[lex] in symbols:
                symbol += lexemes[lex]
                outfile.write("<symbol> " + symbol + " </symbol>\n")
                symbol = ""
            thing = ""
        #Iterate
        lex = lex+1
    #Write the ending header
    outfile.write("</tokens>")

#Open Main.jack, add every character into an array of strings, open an XML outfile, and get to work!
infile = open("Main.jack")
lexemes = []
#For each word in the file
for foo in infile:
    #For each character in a word
    for bar in foo:
        #Add character to array
        lexemes.append(bar)
outfile = open("MainT2.xml", "w")
run()
outfile.close()

#Open SquareGame.jack, add every character into an array of strings, open an XML outfile, and get to work!
infile = open("SquareGame.jack")
lexemes = []
#For each word in the file
for foo in infile:
    #For each character in a word
    for bar in foo:
        #Add character to array
        lexemes.append(bar)
outfile = open("SquareGameT2.xml", "w")
run()
outfile.close()