import ASCIITextToArt

if __name__ == "__main__":
    art = ASCIITextToArt.ASCIITextToArt()
    text = art.getMatrix('Text')
    print('Matrix:\n')
    print(text)
    print('\nContent:\n')
    for i in text:
        print(i)