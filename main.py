from Belfoldi import BelfoldiJarat
from JegyFoglalas import JegyFoglalas
from LegiTarsasag import LegiTarsasag
from NemzetkoziJarat import NemzetkoziJarat
import tkinter as tk
from tkinter import messagebox, simpledialog

legitarsasag = LegiTarsasag("PintérAir")

jarat1 = BelfoldiJarat("BA101", "Budapest", '10000')
jarat2 = BelfoldiJarat("BA102", "Debrecen", '10000')
jarat3 = NemzetkoziJarat("NA201", "London", '50000')

legitarsasag.hozzaad_jarat(jarat1)
legitarsasag.hozzaad_jarat(jarat2)
legitarsasag.hozzaad_jarat(jarat3)

foglalaskezelo = JegyFoglalas()

foglalaskezelo.foglalas(jarat1, "Kiss Anna")
foglalaskezelo.foglalas(jarat2, "Nagy Péter")
foglalaskezelo.foglalas(jarat3, "Tóth Gábor")
foglalaskezelo.foglalas(jarat3, "Szabó Éva")
foglalaskezelo.foglalas(jarat1, "Farkas Imre")
foglalaskezelo.foglalas(jarat2, "Kovács Júlia")

def menu():
    while True:
        print("\n--- Repülőjegy Foglalási Rendszer ---")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Válassz műveletet: ")

        if valasztas == "1":
            legitarsasag.listaz_jaratokat()
            jszam = input("Add meg a járatszámot: ")
            nev = input("Add meg az utas nevét: ")
            jarat = next((j for j in legitarsasag.jaratok if j.jaratszam == jszam), None)
            if jarat:
                ar = foglalaskezelo.foglalas(jarat, nev)
                print(f"Foglalás sikeres. Ár: {ar} Ft")
            else:
                print("Nincs ilyen járat.")

        elif valasztas == "2":
            jszam = input("Add meg a lemondandó járatszámot: ")
            nev = input("Add meg az utas nevét: ")
            if foglalaskezelo.lemondas(jszam, nev):
                print("Lemondás sikeres.")
            else:
                print("Nem található ilyen foglalás.")

        elif valasztas == "3":
            foglalaskezelo.listaz_foglalasok()

        elif valasztas == "4":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    menu()
