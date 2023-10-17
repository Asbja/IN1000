from hund import Hund

def hovedProgram():
    hund1 = Hund(13, 5)
    print(hund1.hent_alder(), hund1.hent_vekt(), hund1.metthet)


    for i in range(7):
        hund1.spring()
        print(hund1.metthet, hund1.hent_vekt())


    for i in range(5):
        hund1.spis(3)
        print(hund1.metthet, hund1.hent_vekt())



hovedProgram()