class ASCIITextToArt:
    def __init__(self):
        self.settings = {}
        self.font = {}
        self.setFont("_fonts/default.txt")
        self.setStyles()

    def setStyles(self):
        self.styles = {
            "white":"\033[97m",
            "black":"\033[30m",
            "red":"\033[31m",
            "lightRed":"\033[91m",
            "green":"\033[32m",
            "lightGreen":"\033[92m",
            "yellow":"\033[33m",
            "lightYellow":"\033[93m",
            "blue":"\033[34m",
            "lightBlue":"\033[94m",
            "magenta":"\033[35m",
            "lightMagenta":"\033[95m",
            "cyan":"\033[36m",
            "lightCyan":"\033[96m",
            "gray":"\033[90m",
            "lightGray":"\033[37m",
            "end":"\033[0m",
        }
        

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

    def getStyle(self, style):
        style = style.split()
        appearance = ''

        for element in style:
            if element in self.styles:
                appearance += self.styles[element]

        return appearance

    def getText(self, text, style=''):
        art = ''

        if(self.settings['lowercase'] == 0):
            text = text.lower()

        for i in range(self.settings['height']):
            for letter in text:
                art += self.font[letter][i]
            art += '\n'
        
        art = self.getStyle(style) + art + self.getStyle('end')

        return art

    def getList(self, text, style=''):
        return self.getText(text, style).split('\n')

    def getMatrix(self, text, style=''):
        art = [[i] for i in self.getList(text, style)]
        art.pop()
        return art 

    def printText(self, text, style=''):
        print(self.getText(text, style))

if __name__ == "__main__":
    art = ASCIITextToArt()
    art.printText("ASCII Text", style='lightGray')
    art.printText("To Art", style='lightGray')
    print(art.getStyle('lightGray')+"by:Lucas Antunes de Almeida"+art.getStyle('end'))
