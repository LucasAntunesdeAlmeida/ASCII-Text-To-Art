class ASCIITextToArt:
    def __init__(self):
        self.settings = {}
        self.font = {}
        self.setFont("_fonts/default.txt")

    def setFont(self, file):
        ref_archive = open(file, "r")

        for i in range(3):
            line = ref_archive.readline()
            line = line.split("<>")
            self.settings[line[0]] = int(line[1].replace('\n', ''))
        
        lenFile = (self.settings['symbols']*self.settings['height'])+self.settings['symbols']
        options = {
            'symbol' : self.addSymbol,
            'part' : self.addPart,
        }

        if(self.settings['lowercase'] == 0):
            for i in range(lenFile):
                line = ref_archive.readline()
                line = line.split("<>")
                line[1] = line[1].lower()
                options[line[0]](line)
        else:
            for i in range(lenFile):
                line = ref_archive.readline()
                line = line.split("<>")
                options[line[0]](line)
    
    def addSymbol(self, line):
        self.font[line[1].replace('\n', '')] = []
        for i in range(self.settings['height']):
            self.font[line[1].replace('\n', '')].append([])
    
    def addPart(self, line):
        self.font[line[1]][int(line[2])] = line[3].replace('\n', '')

    def showFont(self):
        for i in self.font:
            print(i)
            for j in range(self.settings['height']):
                print(self.font[i][j])

    def getText(self, text):
        art = ''

        if(self.settings['lowercase'] == 0):
            text = text.lower()

        for i in range(self.settings['height']):
            for letter in text:
                art += self.font[letter][i]
            art += '\n'
        
        return art

    def getList(self, text):
        return self.getText(text).split('\n')

    def getMatrix(self, text):
        art = [[i] for i in self.getList(text)]
        art.pop()
        return art 

    def printText(self, text):
        print(self.getText(text))

if __name__ == "__main__":
    art = ASCIITextToArt()
    art.printText("ASCII Text")
    art.printText("To Art")
    print("by:Lucas Antunes de Almeida")
