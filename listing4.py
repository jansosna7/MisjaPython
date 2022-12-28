# Escape - Misja Python
# Autor: Sean <c<amus / www.sean.co.uk
# Wpisał: Jan Sosnowski

import time, random, math

#############
#  ZMIENNE  #
#############

WIDTH = 800
HEIGTH = 800

#zmienne gracza
IMIE_GRACZA = "JAN"
IMIE_PRZYJACIELA1 = "KAREN"
IMIE_PRZYJACIELA2 = "LEO"
aktualny_pokuj = 31

gora_lewa_x = 100
gora_lewa_y = 150

#OBIEKTY_DEMO = [images.podloga, images.filar, images.gleba]

##########
#  MAPA  #
##########

MAPA_SZEROKOSC = 5
MAPA_WYSOKOSC = 10
MAPA_ROZMIAR = MAPA_WYSOKOSC*MAPA_SZEROKOSC

MAPA_GRY = [["Pokój 0 - magazyn nieużywanych obiektów", 0, 0, False, False]]

pokoje_zewnetrzne = range(1,26)
for sektoryplanety in range(1, 26):
    MAPA_GRY.append(["Zapylona powierzchnia planety", 13, 13, True, True])

MAPA_GRY += [
    #[Nazwa pokoju, wysokość, szerokość górne drzwi, prawe drzwi]
    ["Sluza powierzna", 13, 5, True, False], #pokoj 26
    ["Maszynownia", 13, 13, False, False],#pokoj 27
    ["Centrum sterowania Poodle", 9, 13, False, True],#pokoj 28
    ["Galeria widokowa", 9, 15, False, False],#pokoj 29
    ["Lazienka załogi", 5, 5, False, False],#pokoj 30
    ["Przedsionek do śluzy powitrznej", 7, 11, True, True],#pokoj 31
    ["Pokój z lewym wyjściem", 9, 7, True, False],#pokoj 32
    ["Pokój z prawym wyjściem", 7, 13, True, True],#pokoj 33
    ["Laboratorium", 13, 13, False, True],#pokoj 34
    ["Szklarnia", 13, 13, True, False],#pokoj 35
    ["Sypialnia kpt. " + IMIE_GRACZA, 9, 11, False, False],#pokoj 36
    ["Zachodni korytarz", 15, 5, True, True],#pokoj 37
    ["Sala konferencyjna", 7, 13, False, True],#pokoj 38
    ["Swietlica załogi", 11, 13, True, False],#pokoj 39
    ["Główne centrum strowania", 14, 14, False, False],#pokoj 40
    ["Izba chorych", 12, 7, True, False],#pokoj 41
    ["Zachodni korytarz", 9, 7, True, False],#pokoj 42
    ["Centrum infrastruktury technicznej", 9, 9, False, True],#pokoj 43
    ["Centrum zarządzania systemami", 9, 11, False, False],#pokoj 44
    ["Wejście do centrum sterowania", 7, 7, True, False],#pokoj 45
    ["Sypialnia płk. " + IMIE_PRZYJACIELA1, 9, 11, True, True],#pokoj 46
    ["Sypialnia płk. " + IMIE_PRZYJACIELA2, 9, 11, True, True],#pokoj 47
    ["Pokój z systemem rur", 13, 11, True, False],#pokoj 48
    ["Biuro głównego naukowca", 9, 7, True, True],#pokoj 49
    ["Warsztat robotów", 9, 11, True, False]#pokoj 50
]

assert len(MAPA_GRY)-1 == MAPA_ROZMIAR, "Rozmiar mapy nie pasuje do MAPA_GRY"