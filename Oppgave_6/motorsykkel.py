class Motorsykkel:
    def __init__(self, merke, registreringsnummer):
        self.kilometeravstand = 0
        self.merke = merke
        self.registreringsnummer = registreringsnummer
        
    def kjor(self, km):
        self.kilometeravstand += km

    def hent_kilometeravstand(self):
        return self.kilometeravstand

    def skriv_ut(self):
        print(self.merke, self.registreringsnummer, self.kilometeravstand)