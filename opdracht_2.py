class dna:

    def __init__(self, dna_sequentie):
        self.__dna_sequentie = dna_sequentie

    def setdna(self, dna_sequentie):
        if re.search("[ATCGN]*", dna_sequentie):
            self.__dna_sequentie = dna_sequentie
        else:
            print("dit is geen dna sequentie")

    def getdna(self,):
        return self.__dna_sequentie

    def gettranscript(self):
        return self.__rna_sequentie

    def getlength(self):
        return self.__length

    def getgc_percentage(self):
        return self.__gc_percentage

def main():

main()
