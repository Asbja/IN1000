class Hund:
    def __init__(self, alder, vekt):
        self.alder = alder
        self.vekt = vekt
        self.metthet = 10

    def hent_alder(self):
        return self.alder
    
    def hent_vekt(self):
        return self.vekt
    
    def spring(self):
        self.metthet -= 1
    
        if self.metthet < 5:
            self.vekt -= 1

    def spis(self, mengde):
        self.metthet += mengde

        if self.metthet > 7:
            self.vekt += 1

