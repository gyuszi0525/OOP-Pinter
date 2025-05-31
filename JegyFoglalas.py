class JegyFoglalas:
    def __init__(self):
        self.foglalasok = []

    def foglalas(self, jarat, utas_nev):
        self.foglalasok.append((jarat, utas_nev))
        return jarat.jegyar

    def lemondas(self, jaratszam, utas_nev):
        for f in self.foglalasok:
            if f[0].jaratszam == jaratszam and f[1] == utas_nev:
                self.foglalasok.remove(f)
                return True
        return False

    def listaz_foglalasok(self):
        if not self.foglalasok:
            print("Nincs aktív foglalás.")
        for jarat, utas in sorted(self.foglalasok, key=lambda f: f[0].jaratszam):
            print(f"{utas} -> {jarat.info()}")