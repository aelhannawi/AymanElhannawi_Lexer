# Ayman Elhannawi
# Comp-340 homework_5



import Lexer

srcCode="((12+3*5)+5/4)"
tokSeq= Lexer.tokenize(srcCode)

for i in tokSeq:
    print(i['type'], i['value'])