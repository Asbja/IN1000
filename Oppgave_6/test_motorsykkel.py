from motorsykkel import Motorsykkel

def hovedprogram():
    motorsykkel1 = Motorsykkel("Toyota", 4321)
    motorsykkel1.skriv_ut()

    motorsykkel2 = Motorsykkel("BMW", 1243)
    motorsykkel2.skriv_ut()

    motorsykkel3 = Motorsykkel("Benz", 5324)
    motorsykkel3.skriv_ut()

    motorsykkel3.kjor(10)
    print(motorsykkel3.hent_kilometeravstand())



hovedprogram()