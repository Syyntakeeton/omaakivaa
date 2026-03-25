import random
from datetime import date
tunnuslista = []




class Käyttäjä:
    def __init__(self,tunnus:int,aloitus_pvm):
        self.tunnus = tunnus
        self.aloitus_pvm = aloitus_pvm
        self.arvostelut = {}

    def lisää_osoite(self,osoite:str):#kesken
        self.osoite = osoite

    def lisää_etunimi(self,nimi:str):
        if isinstance(nimi,str):
            self.etunimi = nimi
            return True
        else:
            return False

    def lisää_sukunimi(self,nimi:str):
        if isinstance(nimi,str):
            self.sukunimi = nimi
            return True
        else:
            return False 

    def lisää_arvio(self,numero:float,arvioija:Käyttäjä):
        if isinstance(numero,float) and numero >= 0.0 and numero <= 5.0:
            self.arvostelut[arvioija.tunnus] = numero
            return True
        else:
            print("arviossa annettu väärä arvo")
            return False

    def arvio(self):
        yhteen = 0
        for arvo in self.arvostelut:
            yhteen += self.arvostelut[arvo]
        keskiarvo = yhteen/len(self.arvostelut)
        return keskiarvo

    def __str__(self):
        return f"{self.tunnus} {self.aloitus_pvm}"


def luo_käyttäjä():
    yymmdd = date.today()#aloitus pvm
    ddmmyy = yymmdd.strftime("%d/%m/%Y")#str
    while True:
        tunnus = random.random()
        if tunnus not in tunnuslista:
            break
    uusi_käyttäjä = Käyttäjä(tunnus,ddmmyy)

#    while True:
#        #funktiokutsu fronttiin
#        nimi = input("Anna etunimi")
#        if uusi_käyttäjä.lisää_etunimi(nimi):
#            print("gg")
#            break
#        print("nimi sopimaton")

    

luo_käyttäjä()