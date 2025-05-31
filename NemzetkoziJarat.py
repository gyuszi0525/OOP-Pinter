from Jarat import Jarat
class NemzetkoziJarat (Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    def info(self):
        return f"Nemzetközi járat: {self.jaratszam} -> {self.celallomas}, Ár: {self.jegyar} Ft"