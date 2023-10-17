class Dato:
    def __init__(self, ny_dag, ny_maaned, nytt_aar):
        self.dag = ny_dag
        self.maaned = ny_maaned
        self.aar = nytt_aar


    def hent_aar(self):
        return self.aar
    

    def skriv_dato(self):
        return (f"Datoen idag er: {self.dag}.{self.maaned}.{self.aar}")


    def riktig_dag(self, dag_nr):
        if dag_nr == self.dag:
            return True
        

    def sammenlign_dato(self, nyDato):
        if self.aar < nyDato.aar:
            print("Den nye datoen er etter den orginale.")

        elif self.aar == nyDato.aar:

            if self.maaned < nyDato.maaned:
                print("Den nye datoen er etter den orginale.")

            elif self.maaned == nyDato.maaned:

                if self.dag < nyDato.dag:
                    print("Den nye datoen er etter den orginale.")

                elif self.dag == nyDato.dag:
                    print("Det er samme dato")

                else:
                    print("Den nye datoen er før den orginale datoen.")

            else:
                print("Den nye datoen er før den orginale.")

        else:
            print("Den nye datoen er før den orginale.")

    
    def nesteDato(self, maaneder):
        if self.maaned in maaneder[0]:
            if self.dag == 31:
                self.maaned += 1
                self.dag = 1
            else:
                self.dag += 1
        
        elif self.maaned in maaneder[1]:
            if self.dag == 30:
                self.maaned += 1
                self.dag = 1
            else:
                self.dag += 1
        
        elif self.maaned == 2:
            if self.aar % 4 == 0:
                if self.dag == 29:
                    self.maaned += 1
                    self.dag = 1
                else:
                    self.dag += 1
            else:
                if self.dag == 28:
                    self.maaned += 1
                    self.dag = 1
                else:
                    self.dag += 1

        else:
            if self.dag == 31:
                self.aar += 1
                self.maaned = 1
                self.dag = 1
            else:
                self.dag += 1
                    

