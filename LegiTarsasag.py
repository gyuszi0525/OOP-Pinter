class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def hozzaad_jarat(self, jarat):
        self.jaratok.append(jarat)

    def listaz_jaratokat(self):
        for jarat in self.jaratok:
            print(jarat.info())