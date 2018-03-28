import os
from writer import writer

def cleantext():
    os.system('cls' if os.name == 'nt' else 'clear')

def charactersmap(text):
    characters = {
        "a" : 0,
        "b" : 1,
        "c" : 2,
        "d" : 3,
        "e" : 4,
        "f" : 5,
        "g" : 6,
        "h" : 7,
        "i" : 8,
        "j" : 9,
        "k" : 10,
        "l" : 11,
        "m" : 12,
        "n" : 13,
        "o" : 14,
        "p" : 15,
        "q" : 16,
        "r" : 17,
        "s" : 18,
        "t" : 19,
        "u" : 20,
        "v" : 21,
        "w" : 22,
        "x" : 23,
        "y" : 24,
        "z" : 25,
        " " : 26,
        "1" : 27,
        "2" : 28,
        "3" : 29,
        "4" : 30,
        "5" : 31,
        "6" : 32,
        "7" : 33,
        "8" : 34,
        "9" : 35,
        "0" : 36,
        "!" : 37,
        "@" : 38,
        "#" : 39,
        "$" : 40,
        "%" : 41,
        "&" : 42,
        "*" : 43,
        "(" : 44,
        ")" : 45,
        "-" : 46,
        "_" : 47,
        "." : 48,
        "," : 49,
        ":" : 50,
    }
    return characters[text];

def transcriber(Text, mode):
    #controls the height
    for i in range(6):
        print(mode, end="")
        #controls the selected element
        for j in range(len(Text)):
            writer(charactersmap(Text[j]), i)
        print()

def means():
    print(" Do you want a conversion in the form of a comment?")
    opc = input(" Y or N: ").lower()

    if(opc == "y"):
        print(" Enter the symbols ")
        print(" Example: for a comment in python enter #")
        mode = input(" Symbols: ")
    else:
        mode = " "

    if(mode != " "):
        mode = " " + mode + " "

    print()
    
    return mode

def transcriberinline():
    cleantext()
    Text = input(" Input Text: ")
    Text = Text.lower()

    transcriber(Text, means())

def transcriberinmultiple():
    cleantext()
    lines = int(input(" Number of lines: "))

    Text = []

    for i in range(lines):
        print(" Input Text[", i, "]: ", end="")
        Text.append(input().lower())

    mode = means()

    for i in range(lines):
        transcriber(Text[i], mode)

def character(lim1, lim2):
    for i in range(6):
        print(" ", end="")
        for j in range(lim1, lim2):
            writer(j, i)
            writer(26, i)
        print()
    print()

def allcharactersinline():
    cleantext()

    print("\n All characters supported:\n")

    #supported letters
    character(0, 9)
    character(9, 18)
    character(18, 26)

    #supported numbers
    character(27,37)

    #supported special characters
    character(38,51)

    input("Press ENTER key to continue")
    menu()

def allcharactersincolumn():
    cleantext()

    print("\n All characters supported:\n")

    #allcharacters
    for i in range(0, 51):
        character(i, i+1)

    input("Press ENTER key to continue")
    menu()

def logo():
        cleantext()

        print('                                                                      ')
        print('  █████╗ ███████╗ ██████╗██╗██╗    ████████╗███████╗██╗  ██╗████████╗ ')
        print(' ██╔══██╗██╔════╝██╔════╝██║██║    ╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝ ')
        print(' ███████║███████╗██║     ██║██║       ██║   █████╗   ╚███╔╝    ██║    ')
        print(' ██╔══██║╚════██║██║     ██║██║       ██║   ██╔══╝   ██╔██╗    ██║    ')
        print(' ██║  ██║███████║╚██████╗██║██║       ██║   ███████╗██╔╝ ██╗   ██║    ')
        print(' ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝    ')
        print(' ████████╗ ██████╗      █████╗ ██████╗ ████████╗                      ')
        print(' ╚══██╔══╝██╔═══██╗    ██╔══██╗██╔══██╗╚══██╔══╝                      ')
        print('    ██║   ██║   ██║    ███████║██████╔╝   ██║                         ')
        print('    ██║   ██║   ██║    ██╔══██║██╔══██╗   ██║                         ')
        print('    ██║   ╚██████╔╝    ██║  ██║██║  ██║   ██║                         ')
        print('    ╚═╝    ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝                         ')
        print(' By: Lucas Antunes de Almeida                                         ')
        print('                                                                      ')

def menu():
    logo()
    options = {
        0 : transcriberinline,
        1 : transcriberinmultiple,
        2 : allcharactersinline,
        3 : allcharactersincolumn,
        4 : exit,
    }

    print(" [0] ASCII text converter for art in line")
    print(" [1] ASCII text converter for art in multiple lines")
    print(" [2] Display all characters supported in line")
    print(" [3] Display all characters supported in column")
    print(" [4] Exit")

    opc = int(input(" Selected option: "))

    if(opc >= 0 and opc < 5):
        options[opc]()


def main():
    menu()

if __name__ == '__main__':
    main()
