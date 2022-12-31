# Escape - Misja Python
# Autor: Sean <c<amus / www.sean.co.uk
# Wpisał: Jan Sosnowski

import time, random, math

#import movement as movement
#from pgzero import *

#############
#  ZMIENNE  #
#############
#from pgzero.clock import clock
#from pgzero.game import screen
#from pgzero.keyboard import keyboard

WIDTH = 800
HEIGTH = 800

# zmienne gracza
IMIE_GRACZA = "JAN"
IMIE_PRZYJACIELA1 = "KAREN"
IMIE_PRZYJACIELA2 = "LEO"
aktualny_pokoj = 31

gora_lewa_x = 100
gora_lewa_y = 150

OBIEKTY_DEMO = [images.podloga, images.filar, images.gleba]

##########
#  MAPA  #
##########

MAPA_SZEROKOSC = 5
MAPA_WYSOKOSC = 10
MAPA_ROZMIAR = MAPA_WYSOKOSC * MAPA_SZEROKOSC

MAPA_GRY = [["Pokój 0 - magazyn nieużywanych obiektów", 0, 0, False, False]]

pokoje_zewnetrzne = range(1, 26)
for sektoryplanety in range(1, 26):
    MAPA_GRY.append(["Zapylona powierzchnia planety", 13, 13, True, True])

MAPA_GRY += [
    # [Nazwa pokoju, wysokość, szerokość górne drzwi, prawe drzwi]
    ["Sluza powierzna", 13, 5, True, False],  # pokoj 26
    ["Maszynownia", 13, 13, False, False],  # pokoj 27
    ["Centrum sterowania Poodle", 9, 13, False, True],  # pokoj 28
    ["Galeria widokowa", 9, 15, False, False],  # pokoj 29
    ["Lazienka załogi", 5, 5, False, False],  # pokoj 30
    ["Przedsionek do śluzy powitrznej", 7, 11, True, True],  # pokoj 31
    ["Pokój z lewym wyjściem", 9, 7, True, False],  # pokoj 32
    ["Pokój z prawym wyjściem", 7, 13, True, True],  # pokoj 33
    ["Laboratorium", 13, 13, False, True],  # pokoj 34
    ["Szklarnia", 13, 13, True, False],  # pokoj 35
    ["Sypialnia kpt. " + IMIE_GRACZA, 9, 11, False, False],  # pokoj 36
    ["Zachodni korytarz", 15, 5, True, True],  # pokoj 37
    ["Sala konferencyjna", 7, 13, False, True],  # pokoj 38
    ["Swietlica załogi", 11, 13, True, False],  # pokoj 39
    ["Główne centrum strowania", 14, 14, False, False],  # pokoj 40
    ["Izba chorych", 12, 7, True, False],  # pokoj 41
    ["Zachodni korytarz", 9, 7, True, False],  # pokoj 42
    ["Centrum infrastruktury technicznej", 9, 9, False, True],  # pokoj 43
    ["Centrum zarządzania systemami", 9, 11, False, False],  # pokoj 44
    ["Wejście do centrum sterowania", 7, 7, True, False],  # pokoj 45
    ["Sypialnia płk. " + IMIE_PRZYJACIELA1, 9, 11, True, True],  # pokoj 46
    ["Sypialnia płk. " + IMIE_PRZYJACIELA2, 9, 11, True, True],  # pokoj 47
    ["Pokój z systemem rur", 13, 11, True, False],  # pokoj 48
    ["Biuro głównego naukowca", 9, 7, True, True],  # pokoj 49
    ["Warsztat robotów", 9, 11, True, False]  # pokoj 50
]

assert len(MAPA_GRY) - 1 == MAPA_ROZMIAR, "Rozmiar mapy nie pasuje do MAPA_GRY"


##################
# TWORZENIE MAPY #
##################

def sprawdz_typ_podlogi():
    if aktualny_pokoj in pokoje_zewnetrzne:
        return 2  # gleba
    else:
        return 0  # kafelki


def generuj_mape():
    global mapa_pokoju, szer_pokoju, wys_pokoju, nazwa_pokoju
    global mapa_zagrozen, gora_lewa_x, gora_lewa_y
    global ramka_przezroczystosci_sciany
    dane_pokoju = MAPA_GRY[aktualny_pokoj]
    nazwa_pokoju = dane_pokoju[0]
    wys_pokoju = dane_pokoju[1]
    szer_pokoju = dane_pokoju[2]

    typ_podlogi = sprawdz_typ_podlogi()
    if aktualny_pokoj in range(1, 21):
        dolny_brzeg = 2  # gleba
        boczny_brzeg = 2  # gleba
    if aktualny_pokoj in range(21, 26):
        dolny_brzeg = 1  # sciana
        boczny_brzeg = 2  # gleba
    if aktualny_pokoj > 25:
        dolny_brzeg = 1  # sciana
        boczny_brzeg = 1  # sciana

    # gorny rząd mapy
    mapa_pokoju = [[boczny_brzeg] * szer_pokoju]
    # dodanie środkowych rzędów mapy pokoju (sciana, pośrodku podłoga ściana
    for y in range(wys_pokoju - 2):
        mapa_pokoju.append([boczny_brzeg] + [typ_podlogi] * (szer_pokoju - 2) + [boczny_brzeg])
    # dolny rząd
    mapa_pokoju.append([dolny_brzeg] * szer_pokoju)

    # dodanie wyjsc
    srodkowy_rzad = int(wys_pokoju / 2)
    srodkowa_kolumna = int(szer_pokoju / 2)

    if dane_pokoju[4]:  # prawe wyjscie
        mapa_pokoju[srodkowy_rzad][szer_pokoju - 1] = typ_podlogi
        mapa_pokoju[srodkowy_rzad + 1][szer_pokoju - 1] = typ_podlogi
        mapa_pokoju[srodkowy_rzad - 1][szer_pokoju - 1] = typ_podlogi

    if aktualny_pokoj % MAPA_SZEROKOSC != 1:
        # jesli pokoj nie lezy po lewej stronie mapy
        pokoj_po_lewej = MAPA_GRY[aktualny_pokoj - 1]
        # jesli pokoj po lewej ma prawe wyjscie dodanie lewego wyjscia w pokoju
        if pokoj_po_lewej[4]:
            mapa_pokoju[srodkowy_rzad][0] = typ_podlogi
            mapa_pokoju[srodkowy_rzad + 1][0] = typ_podlogi
            mapa_pokoju[srodkowy_rzad - 1][0] = typ_podlogi

    if dane_pokoju[3]:
        mapa_pokoju[0][srodkowa_kolumna] = typ_podlogi
        mapa_pokoju[0][srodkowa_kolumna + 1] = typ_podlogi
        mapa_pokoju[0][srodkowa_kolumna - 1] = typ_podlogi

    if aktualny_pokoj <= MAPA_ROZMIAR - MAPA_SZEROKOSC:
        # jesli pokoj nie lezy w dolnym rzedzie
        pokoj_po_nizej = MAPA_GRY[aktualny_pokoj + MAPA_SZEROKOSC]
        # jesli pokoj po nizej ma gorne wyjsie dodanie dolnego wyjscia w pokoju
        if pokoj_po_nizej[3]:
            mapa_pokoju[wys_pokoju - 1][srodkowa_kolumna] = typ_podlogi
            mapa_pokoju[wys_pokoju - 1][srodkowa_kolumna + 1] = typ_podlogi
            mapa_pokoju[wys_pokoju - 1][srodkowa_kolumna - 1] = typ_podlogi


############
# EXPLORER #
############

def draw():
    global wys_pokoju, szer_pokoju, mapa_pokoju
    generuj_mape()
    screen.clear()

    for y in range(wys_pokoju):
        for x in range(szer_pokoju):
            obraz_do_narysowania = OBIEKTY_DEMO[mapa_pokoju[y][x]]
            screen.blit(obraz_do_narysowania,
                        (gora_lewa_x + (x * 30),
                         gora_lewa_y + (y * 30) - obraz_do_narysowania.get_height()))


def ruch():
    global aktualny_pokoj
    stary_pokoj = aktualny_pokoj

    if keyboard.left:
        aktualny_pokoj -= 1
    if keyboard.right:
        aktualny_pokoj += 1
    if keyboard.up:
        aktualny_pokoj -= MAPA_SZEROKOSC
    if keyboard.down:
        aktualny_pokoj += MAPA_SZEROKOSC

    if aktualny_pokoj > 50:
        aktualny_pokoj = 50
    if aktualny_pokoj < 1:
        aktualny_pokoj = 1

    if aktualny_pokoj != stary_pokoj:
        print("wschodzisz do pokoju: " + str(aktualny_pokoj))


clock.schedule_interval(ruch, 0.1)
