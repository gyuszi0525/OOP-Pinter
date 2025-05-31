from Jarat import Jarat
class BelfoldiJarat (Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    def info(self):
        return f"Belföldi járat: {self.jaratszam} -> {self.celallomas}, Ár: {self.jegyar} Ft"