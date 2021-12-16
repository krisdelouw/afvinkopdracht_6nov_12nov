class pet:

    def __init__(self, naam, type, age):
        self.__name = naam
        self.__type = type
        self.__age = age

    def setnaam(self, naam):
        self.__naam = naam

    def getnaam(self):
        return self.__naam

    def setanimal_type(self, animal_type):
        self.__animal_type = animal_type

    def getanimal_type(self):
        return self.__animal_type

    def setage(self, age):
        self.__age = age

    def getage(self):
        return self.__age


def main():
    hond = pet("ginger", "hond", 10)
    print(vars(hond))


main()
