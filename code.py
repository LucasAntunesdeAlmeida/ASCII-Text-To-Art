import os
from writer import writer

def transcriber():
    Text = input(" Input Text: ")
    aux = 2;

    print()
    #controls the height
    for i in range(6):
        print(" ", end="")
        #controls the selected element
        for j in range(len(Text)):

            if((Text[j] == "a") or (Text[j] == "A")):
                aux = 0
            elif ((Text[j] == "b") or (Text[j] == "B")):
                aux = 1
            elif ((Text[j] == "c") or (Text[j] == "C")):
                aux = 2
            elif ((Text[j] == "d") or (Text[j] == "D")):
                aux = 3
            elif ((Text[j] == "e") or (Text[j] == "E")):
                aux = 4
            elif ((Text[j] == "f") or (Text[j] == "F")):
                aux = 5
            elif ((Text[j] == "g") or (Text[j] == "G")):
                aux = 6
            elif ((Text[j] == "h") or (Text[j] == "H")):
                aux = 7
            elif ((Text[j] == "i") or (Text[j] == "I")):
                aux = 8
            elif ((Text[j] == "j") or (Text[j] == "J")):
                aux = 9
            elif ((Text[j] == "k") or (Text[j] == "K")):
                aux = 10
            elif ((Text[j] == "l") or (Text[j] == "L")):
                aux = 11
            elif ((Text[j] == "m") or (Text[j] == "M")):
                aux = 12
            elif ((Text[j] == "n") or (Text[j] == "N")):
                aux = 13
            elif ((Text[j] == "o") or (Text[j] == "O")):
                aux = 14
            elif ((Text[j] == "p") or (Text[j] == "P")):
                aux = 15
            elif ((Text[j] == "q") or (Text[j] == "Q")):
                aux = 16
            elif ((Text[j] == "r") or (Text[j] == "R")):
                aux = 17
            elif ((Text[j] == "s") or (Text[j] == "S")):
                aux = 18
            elif ((Text[j] == "t") or (Text[j] == "T")):
                aux = 19
            elif ((Text[j] == "u") or (Text[j] == "U")):
                aux = 20
            elif ((Text[j] == "v") or (Text[j] == "V")):
                aux = 21
            elif ((Text[j] == "w") or (Text[j] == "W")):
                aux = 22
            elif ((Text[j] == "x") or (Text[j] == "X")):
                aux = 23
            elif ((Text[j] == "y") or (Text[j] == "Y")):
                aux = 24
            elif ((Text[j] == "z") or (Text[j] == "Z")):
                aux = 25
            else:
                aux = 26
            writer(aux, i)
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
