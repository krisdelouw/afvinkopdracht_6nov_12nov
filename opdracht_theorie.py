import re


class student:

    def __init__(self, voornaam, achternaam):
        self.__voornaam = voornaam
        self.__achternaam = achternaam

    def setvoornaam(self, voornaam):
        if re.search("[A-Z][a-z]*", voornaam):
            self.__voornaam = voornaam
        else:
            print("dit is geen voornaam ")

    def getvoornaam(self):
        return self.__voornaam

    def setachternaam(self, achternaam):
        if achternaam[0].upper() and achternaam[1:].lower():
            self.__achternaam = achternaam
        else:
            print("dit is geen achternaam")

    def getachternaam(self):
        return self.__achternaam

    def setwoonplaats(self, woonplaats):
        if re.search("[A-Z][a-z]*", woonplaats):
            self.__woonplaats = woonplaats
        else:
            print("dit is geen woonplaats ")

    def getwoonplaats(self):
        return self.__woonplaats

    def setadress(self, straatnaam, huisnummer):
        if re.search("[A-Z][a-z]*", straatnaam):
            self.__straatnaam = straatnaam
        else:
            print("dit is geen straatnaam ")
        if re.search("[0-9]*[A-Z]?", huisnummer):
            self.__huisnummer = huisnummer
        else:
            print("dit is geen huisnummer ")

    def getadress(self):
        return "".join([self.__straatnaam, self.__huisnummer])

    def setnummer(self, nummer):
        if re.search("(06|00316|\+316)[0-9]{8}", nummer):
            self.__nummer = nummer
        else:
            print("dit is geen nummer ")

    def getnummer(self):
        return self.__nummer

    def setpostcode(self, postcode):
        if re.search(r"[1-9]\d{3}\s?[a-zA-Z]{2}", postcode):
            self.__postcode = postcode
        else:
            print("dit is geen postcode, hou het volgende aan: 1000 HH")

    def getpostcode(self):
        return self.__postcode

    def setopleiding(self, opleiding):
        self.__opleiding = opleiding

    def getopleiding(self):
        return self.__opleiding

    def setklas(self, klas):
        if re.search("[A-Z]{3}[1-9][A-Z]", klas):
            self.__klas = klas
        else:
            print("dit is geen klas ")

    def getklas(self):
        return self.__klas

    def setslber(self, slber):
        if re.search("[A-Z][a-z]*", slber):
            self.__slber = slber
        else:
            print("dit is geen slb'er")

    def getslber(self):
        return self.__slber

    def setgeboortedatum(self, geboortedatum):
        if re.search("[0-9]{2}[0-9]{2}[0-9]{4}", geboortedatum):
            self.__geboortedatum = geboortedatum
        else:
            print("dit is geen geboortedatum")

    def getgeboortedatum(self):
        return self.__geboortedatum


def main():
    student0 = student("Ambra", "Hovenier")
    print(student0.getvoornaam(), student0.getachternaam())
    student1 = student()
    student1.setvoornaam("Kris")
    print(student1.getvoornaam())
    student1.setachternaam("de Louw")
    print(student1.getachternaam())
    student1.setwoonplaats("Nijmegen")
    print(student1.getwoonplaats())
#    student1.setadress("Gemsstraat 13")
#    print(student1.getadress())
    student1.setnummer("0651889196")
    print(student1.getnummer())
    student1.setpostcode("6531TC")
    print(student1.getpostcode())
    student1.setopleiding("Bio informatica")
    print(student1.getopleiding())
    student1.setklas("BIN1C")
    print(student1.getklas())
    student1.setslber("Ruben")
    print(student1.getslber())
    student1.setgeboortedatum("07082003")
    print(student1.getgeboortedatum())


main()
