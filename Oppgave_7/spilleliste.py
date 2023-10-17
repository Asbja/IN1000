from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def les_fra_fil(self, ny_sang):
         fil = open("musikk.txt")