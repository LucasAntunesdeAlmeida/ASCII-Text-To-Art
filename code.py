import os
from writer import writer

def transcriber():
    Text = input(" Input Text: ")
    Text = Text.lower()

    print()
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
        " " : 26
    }

    #controls the height
    for i in range(6):
        print(" ", end="")
        #controls the selected element
        for j in range(len(Text)):
            writer(characters[Text[j]], i)
        print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

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

    transcriber()

if __name__ == '__main__':
    main()
