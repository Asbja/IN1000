from dato import Dato

def hovedprogram():
    dato = Dato(15, 11, 22)

    print(dato.hent_aar())


    if dato.riktig_dag(15):
        print("Lønningsdag!")
    
    if dato.riktig_dag(1):
        print("Ny måned, nye muligheter!")

    
    idag = dato.skriv_dato()
    print(idag)


    maaneder = [[1, 3, 5, 7, 8, 10], [4, 6, 9, 11]]
    dato.nesteDato(maaneder)

    idag = dato.skriv_dato()
    print(idag)


    dato2 = Dato(16, 4, 23)
    dato.sammenlign_dato(dato2)

hovedprogram()