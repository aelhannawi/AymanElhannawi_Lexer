# Ayman Elhannawi
# Comp-340 homework_5



def tokenize(srcCode):
    tokSeq = []
    for i in range(len(srcCode)):
        char ={}
        if srcCode[i].isdigit(): #Return the Integer.
            if srcCode[i-1].isdigit():
                continue
            empty = ""
            while srcCode[i].isdigit():
                empty += srcCode[i]
                i += 1
            char["type"] = "NUMBER"
            char["value"] = empty
        elif srcCode[i] == "+": #Return Plus
            char["type"]= "PLUS"
            char["value"] = srcCode[i]
        elif srcCode[i] == "-": #Return Minus
            char["type"] = "MINUS"
            char["value"] =srcCode[i]
        elif srcCode[i] == "*": #Return Multiplication
            char["type"] = "MULTIPLICATION"
            char["value"] = srcCode[i]
        elif srcCode[i] == "/": #Return Division
            char["type"] = "DIVISION"
            char["value"] = srcCode[i]
        elif srcCode[i] == "(": #Return Left Paren
            char["type"] = "LPAREN"
            char["value"] = srcCode[i]
        elif srcCode[i] == ")": #Return Right Paren
            char["type"] = "RPAREN"
            char["value"] = srcCode[i]

        tokSeq.append(char) #Store The value

    return tokSeq #Return the value.