import os
import ASCIITextToArt

def cleantext():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system("clear && printf '\e[3J'" if os.name == 'nt' else "clear && printf '\e[3J'")

def exitMenu(art):
    cleantext()
    exit()

def menu(art):
    cleantext()
    art.printText(" ASCII Text")
    art.printText("   To Art")

    options = {
        '0' : menu,
        '1' : menu,
        '2' : menu,
        '3' : menu,
        '4' : exitMenu,
    }

    print(" [0] Menu")
    print(" [1] Menu")
    print(" [2] Menu")
    print(" [3] Menu")
    print(" [4] Exit")

    opc = input(" Selected option: ")
    if opc in options:
        options[opc](art)
    else:
        menu(art)

if __name__ == "__main__":
    art = ASCIITextToArt.ASCIITextToArt()
    menu(art)
    