# Ohjelmoinnin perusteet teht 6.2
# Lari Wihuri
# 07.10.2026

from machine import Pin, PWM
from time import sleep

# Motor A / Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Motor B / Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Set PWM frequency to 1000 Hz / Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)

# Aika, joka ajetaan suoraan n. puoli metriä
ajoAika = 2.5

# Aika, joka käytetään kääntymiseen n. 90 astetta
kaantymisAika = 0.75

# Maksiminpeus = 65534

# Moottorien nopeus 0-100 arvoksi
def nopeudenVaihto(prosentti):
    nopeus = int((prosentti / 100) * 65534) # Kerrotaan moottorien maksimiarvo kokonaisluvulla 0-100
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)

def eteen(aika):
    m1.value(1)
    m2.value(1)
    sleep(aika)

def taakse(aika):
    m1.value(0)
    m2.value(0)
    sleep(aika)

def vasen(aika):
    m1.value(1)
    m2.value(0)
    sleep(aika)

def oikea(aika):
    m1.value(0)
    m2.value(1)
    sleep(aika)

def pysahdy():
    nopeudenVaihto(0)

# Luetaan ohjetiedosto ja suoritetaan komennot
def suorita_reitti(ohjeet):
    try:
        with open(ohjeet, "r") as reitti:
            for rivi in reitti:

                # Komento autolle ohjetiedostosta
                komento = rivi.strip().lower()

                print("Suoritetaan komento: ", komento)

                # Nopeus
                nopeudenVaihto(60)

                if komento == "eteen":
                    eteen(ajoAika)
                elif komento == "taakse":
                    taakse(ajoAika)
                elif komento == "vasen":
                    vasen(kaantymisAika)
                elif komento == "oikea":
                    oikea(kaantymisAika)
                elif komento == "ympari":
                    vasen(kaantymisAika*2)
                else:
                    print("Tuntematon komento ohjeissa.")

                pysahdy()
                sleep(0.5) # Tauko komentojen välissä
    except:
        print("Virhe ohjetiedoston avauksessa.")

# Varmistetaan että auto on pysähtynyt aluksi
pysahdy() 

# 2 sekunnin tauko ennen kuin ohjelma suorittuu
sleep(2)

# Luetaan reittiohjeet ja suoritetaan komennot
suorita_reitti("ohjeet.txt")

# Pysähdytään lopuksi
pysahdy()
print("Ajo suoritettu.")
    

