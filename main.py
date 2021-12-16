class fasta:

    def setheader(self, header):
        if ">" in header:
            self.__header = header
        else:
            print("dit is geen header")

    def getheader(self):
        return self.__header

    def setsequentie(self, sequentie):
        self.__sequentie = sequentie

    def getsequentie(self):
        return self.__sequentie


def main():
    f1 = fasta()
    f1.setheader(">sequentie1")
    print(f1.getheader())
    print(f1)

    f2 = fasta()
    f2.setheader(">sequentie2")
    print(f2.getheader())


main()
