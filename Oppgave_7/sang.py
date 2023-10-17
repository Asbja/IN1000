class Sang:
    def __init__(self, tittel, artist):
        self.tittel = tittel
        self.artist = artist


    def spill(self):
        print(f"Nå spilles {self.tittel} med {self.artist}")


    def sjekk_artist(self, navn):
        for el in self.artist.lower().split(" "):
            for ord in navn.lower().split(" "):
                if ord == el:
                    return True
            
        return False
    
    
    def sjekk_tittel(self, tittel):
        if self.tittel.lower() == tittel.lower():
            return True
    
        return False
    
    def sjekk_artist_og_tittel(self, artist, tittel):
        if self.sjekk_artist(artist) and self.sjekk_tittel(tittel):
            return True
        
        return False
    
    def streng_til_fil(self):
        return (f"{self.tittel};{self.artist}\n")


