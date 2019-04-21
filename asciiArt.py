class asciiArt:
    def __init__(self):
        self.settings = {}
        self.font = {}
        self.setFont("fonts/default.txt")

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

if __name__ == "__main__":
    art = asciiArt()
    art.showFont()