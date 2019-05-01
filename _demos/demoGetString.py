import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import ASCIITextToArt

if __name__ == "__main__":
    art = ASCIITextToArt.ASCIITextToArt()
    text = art.getText('Text')
    print(text)    