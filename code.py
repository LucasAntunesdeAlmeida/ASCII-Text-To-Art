import os
from writer import writer, charactersmap

def cleantext():
    os.system('cls' if os.name == 'nt' else 'clear')

def waitaction():
    input("Press ENTER to return to the menu")
    menu()

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

    waitaction()

def transcriberinmultiple():
    cleantext()
    #lines = int(input(" Number of lines: "))

    Text = []

    cont = 0
    while(1):
        print(" Press ENTER to continue or enter part[", cont, "] of the text: ", end="")
        Text.append(input().lower())
        if(Text[cont] == ''):
            break
        cont = cont + 1

    mode = means()

    for i in range(cont):
        transcriber(Text[i], mode)

    waitaction()

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

    waitaction()

def allcharactersincolumn():
    cleantext()

    print("\n All characters supported:\n")

    #allcharacters
    for i in range(0, 51):
        character(i, i+1)

    waitaction()

def logo():
        cleantext()
        print()
        transcriber("ascii text", " ")
        transcriber("to art", " ")
        print(" By: Lucas Antunes de Almeida ")
        print()

def menu():
    logo()
    options = {
        '0' : transcriberinline,
        '1' : transcriberinmultiple,
        '2' : allcharactersinline,
        '3' : allcharactersincolumn,
        '4' : exit,
    }

    print(" [0] ASCII text converter for art in line")
    print(" [1] ASCII text converter for art in multiple lines")
    print(" [2] Display all characters supported in line")
    print(" [3] Display all characters supported in column")
    print(" [4] Exit")

    opc = input(" Selected option: ")

    if opc in options:
        options[opc]()
    else:
        menu()

def main():
    menu()

if __name__ == '__main__':
    main()
