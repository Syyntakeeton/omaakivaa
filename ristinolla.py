#ristinolla
#taulu = [" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "]

import random

class Ristinolla:
    def __init__(self):
        self.taulu = {"1":" _ ","2":" _ ","3":" _ ","4":" _ ","5":" _ ","6":" _ ","7":" _ ","8":" _ ","9":" _ "}
        self.x = " x "
        self.o = " o "

    def taulu_palautus(self):
        print("ok")
        return self.taulu

    def lisää(self,arvo):
        self.arvo = arvo
        if self.taulu[arvo] == " _ ":
            self.taulu[arvo] = " x "
            print("käypä")
            return True
        else:
            return False

    def print(self):
        laskuri = 1
        rivi = ""


    def aloita(self):
        pass

    def tarkista_x(self):#x
        if self.taulu["1"] == self.x:
            if self.taulu["4"] == self.x and self.taulu["7"] == self.x:
                return True
        if self.taulu["2"] == self.x:
            if self.taulu["5"] == self.x and self.taulu["8"] == self.x:
                return True
        if self.taulu["3"] == self.x:
            if self.taulu["6"] == self.x and self.taulu["9"] == self.x:
                return True


        if self.taulu["1"] == self.x:
            if self.taulu["2"] == self.x and self.taulu["3"] == self.x:
                return True
        if self.taulu["4"] == self.x:
            if self.taulu["5"] == self.x and self.taulu["6"] == self.x:
                return True
        if self.taulu["7"] == self.x:
            if self.taulu["8"] == self.x and self.taulu["9"] == self.x:
                return True


        if self.taulu["1"] == self.x:
            if self.taulu["5"] == self.x and self.taulu["9"] == self.x:
                return True
        if self.taulu["3"] == self.x:
            if self.taulu["5"] == self.x and self.taulu["7"] == self.x:
                return True

    def vastus(self):
        nolla = int
        while True:
            nolla = random.randint(1,9)
            if self.taulu[str(nolla)] == " _ ":
                self.taulu[str(nolla)] = " o "
                return True
                break

ristinolla = Ristinolla()
#print(ristinolla.taulu_palautus())

while True:
    laskuri = 1
    rivi = ""
    
    while laskuri <= 9:
        
        
        numero = str(laskuri)
        rivi += ristinolla.taulu[numero]

        #print(taulu[numero])
        if laskuri % 3 == 0:
        
            print(rivi)
            rivi = ""

        laskuri += 1

    lisäys = input("Mihin lisäät?")
    if ristinolla.lisää(lisäys):

        if ristinolla.tarkista_x():
            print("Voitit pelin!")
            break
        else:
            ristinolla.vastus()
            continue


    else:
        print("Valitse uusi kohta")
        continue



    #lisäys
    #if Ristinolla.taulu[lisäys] == " _ ":

        #print("hyväksytty")
        #taulu[lisäys] = " x "


    

    
    #break
    