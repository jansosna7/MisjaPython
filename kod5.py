# Escape - Misja Python
# Autor: Sean <c<amus / www.sean.co.uk
# Wpisał: Jan Sosnowski

import time, random, math

#############
#  ZMIENNE  #
#############


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

LADOWNIK_SEKTOR = random.randint(1, 24)
LADOWNIK_X = random.randint(2, 11)
LADOWNIK_Y = random.randint(2, 11)

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

###########
# OBIEKTY #
###########

obiekty = {
    0: [images.podloga, None, "Podłoga jest czysta i błyszcząca"],
    1: [images.filar, images.pelny_cien, "Sciana jest gładka i zimna"],
    2: [images.gleba, None, "Wygląda jak pustynia"],
    3: [images.filar_niski, images.polcien, " Sciana jest gładka i zimna"],
    4: [images.lozko, images.polcien, "Czyste i wygodne łóżko"],
    5: [images.stol, images.polcien, "Zrobiony z mocnego plastiku"],
    6: [images.krzeslo_lewe, None, "Krzesło z miękkim siedziskiem"],
    7: [images.krzeslo_prawe, None, "Krzesło z miękkim siedziskiem"],
    8: [images.regal_wysoki, images.pelny_cien, "Regał wypełniony podręcznikami"],
    9: [images.regal_niski, images.polcien, "Regał wypełniony podręcznikami"],
    10: [images.szafka, images.polcien, "Mała szafka do przechowywania przedmiotów osobistych"],
    11: [images.komputer_stacjonarny, images.polcien, "Komputer. Użyj do sprawdzeniastanu powietrza i energii"],
    12: [images.roslina, images.roslina_cien, "Krzaczek truskawki, wyhodowany na stacji"],
    13: [images.elektryczne1, images.polcien, "Systemy elektryczne do zasilania stacji kosmicznej"],
    14: [images.elektryczne2, images.polcien, "Systemy elektryczne do zasilania stacji kosmicznej"],
    15: [images.kaktus, images.kaktus_cien, "Au! Uwazaj na kaktusa!"],
    16: [images.krzew, images.krzew_cien, "Kosmiczna salata. Nieco zwiedla, ale niesamowite, ze rosnie na stacji!"],
    17: [images.rury1, images.rury1_cien, "Rury instalacji do uzdatniania wody"],
    18: [images.rury2, images.rury2_cien, "Rury systemu podtrzymywania zycia"],
    19: [images.rury3, images.rury3_cien, "Rury systemu podtrzymywania zycia"],
    20: [images.drzwi, images.drzwi_cien,
         "Drzwi bezpieczenstwa. Otwierane automatycznie przed astronautami w dzialajacych skafandrach."],
    21: [images.drzwi, images.drzwi_cien,
         "Drzwi sluzy powietrznej. Ze wzgledow bezpieczenstwa, do obslugi wymagaja 2 osob."],
    22: [images.drzwi, images.drzwi_cien, "Zamkniete drzwi. Potrzebna karta dostepu kpt. " + IMIE_GRACZA],
    23: [images.drzwi, images.drzwi_cien, "Zamkniete drzwi. Potrzebna karta dostepu plk. " + IMIE_PRZYJACIELA1],
    24: [images.drzwi, images.drzwi_cien, "Zamkniete drzwi. Potrzebna karta dostepu plk. " + IMIE_PRZYJACIELA2],
    25: [images.drzwi, images.drzwi_cien, "Zamkniete drzwi. Otwierane z glownego centrum sterowania"],
    26: [images.drzwi, images.drzwi_cien, "Zamkniete drzwi w maszynowni."],
    27: [images.mapa, images.pelny_cien,
         "Miejsce katastrofy to sektor: " + str(LADOWNIK_SEKTOR) + " // X: " + str(LADOWNIK_X) + " // Y: " + str(
             LADOWNIK_Y)],
    28: [images.skala_duza, images.skala_duza_cien, "Skala. Jej twarda chropowata powierzchnia przypomina piaskowiec",
         "skala"],
    29: [images.skala_mala, images.skala_mala_cien, "Maly, ale ciezki kawalek marsjanskiej skaly"],
    30: [images.krater, None, "Krater na powierzchni planety"],
    31: [images.ogrodzenie, None, "Ogrodzenie z gazy. Pomaga chronic stacje przed burza piaskowa"],
    32: [images.mechanizm, images.mechanizm_cien, "Jeden z eksperymentow naukowych. Delikatnie wibruje"],
    33: [images.ramie_robota, images.ramie_robota_cien, "Ramie robota, sluzy do podnoszenia ciezarow"],
    34: [images.sedes, images.polcien, "Lsniacy czystoscia sedes"],
    35: [images.zlew, None, "Zlew z biezaca woda", "kran"],
    36: [images.globus, images.globus_cien, "Wielki globus planety. Delikatnie podswietlony od wewnatrz"],
    37: [images.stol_laboratoryjny, None, "Stol laboratoryjny do analizy gleby i pylu planety"],
    38: [images.automat, images.pelny_cien, "Automat. Wymaga uzycia monet.", "automat"],
    39: [images.mata_podlogowa, None, "Czujnik nacisku blokujacy wychodzenie w pojedynke"],
    40: [images.statek_ratowniczy, images.statek_ratowniczy_cien, "Statek ratowniczy!"],
    41: [images.centrum_sterowania_misja, images.centrum_sterowania_misja_cien, "Stanowiska centrum sterowania"],
    42: [images.przycisk, images.przycisk_cien, "Przycisk do otwierania automatycznie zamykanych drzwi w maszynowni"],
    43: [images.tablica, images.pelny_cien, "Tablica uzywana podczas spotkan organizacyjnych"],
    44: [images.okno, images.pelny_cien, "Okno z widokiem na powierzchnie planety"],
    45: [images.robot, images.robot_cien, "Robot sprzatajacy. Wylaczony."],
    46: [images.robot2, images.robot2_cien, "Nieskonfigurowany jeszcze robot do badania powierzchni planety."],
    47: [images.rakieta, images.rakieta_cien, "Jednoosobowy statek jest w naprawie"],
    48: [images.toksyczna_podloga, None, "Toksyczna podloga - nie stawaj na niej!"],
    49: [images.dron, None, "Dron dostawczy"],
    50: [images.kula_energii, None, "Kula energii - niebezpieczna!"],
    51: [images.kula_energii2, None, "Kula energii - niebezpieczna!"],
    52: [images.komputer, images.komputer_cien, "Terminal do zarzadzania systemami stacji kosmicznej."],
    53: [images.notatnik, None, "Notatnik. Ktos cos w nim nagryzmolil.", "notatnik"],
    54: [images.guma_do_zucia, None, "Kawalek klejacej gumy do zucia. Smak truskawkowy.", "guma do zucia"],
    55: [images.yoyo, None, "Zabawka z cienkiej, mocnej linki i plastiku. Sluzy do eksperymentow antygrawitacyjnych",
         "Jojo kpt. " + IMIE_GRACZA],
    56: [images.nitka, None, "Kawalek cienkiej, mocnej linki", "kawalek linki"],
    57: [images.igla, None, "Ostra igla kaktusa", "igla kaktusa"],
    58: [images.igla_z_nitka, None, "Igla kaktusa z przymocowana linka", "igla z linka"],
    59: [images.butla, None, "Butla z tlenem przecieka.", "przeciekajaca butla z tlenem"],
    60: [images.butla, None, "Lata chyba sie trzyma!", "zalatana butla z tlenem"],
    61: [images.lustro, None, "Lustro rzuca aureole swiatla na sciane.", "lustro"],
    62: [images.pojemnik_pusty, None, "Rzadko uzywany pojemnik z lekkiego plastiku", "pojemnik"],
    63: [images.pojemnik_pelny, None, "Ciezki pojemnik wypelniony woda", "pojemnik wypelniony woda"],
    64: [images.szmaty, None, "Tlusta szmata! Podnies tylko jesli musisz!", "tlusta szmata"],
    65: [images.mlotek, None, "Mlotek. Byc moze nadaje sie do rozlupywania ...", "mlotek"],
    66: [images.lyzka, None, "Wielka metalowa łyzka", "lyzka"],
    67: [images.torebka_z_jedzeniem, None, "Saszetka z suszonym jedzeniem. Wymaga wody.", "suszone jedzenie"],
    68: [images.jedzenie, None, "Saszetka z jedzeniem. Uzyj, aby odzyskac 100% energii.",
         "jedzenie gotowe do spozycia"],
    69: [images.ksiazka, None, "Ksiazka ma tytul 'Nie panikuj' napisany duza, uspakajajaca czcionka", "ksiazka"],
    70: [images.odtwarzacz_mp3, None, "Odtwarzacz MP3, z najnowszymi hitami", "odtwarzacz MP3"],
    71: [images.ladownik, None, "Poodle, maly statek do eksploracji kosmosu. Jego czarne pudelko zawiera radio.",
         "ladownik Poodle"],
    72: [images.radio, None, "System komunikacji radiowej z ladownika Poodle", "radio do komunikacji"],
    73: [images.modul_gps, None, "Modul GPS", "modul GPS"],
    74: [images.system_pozycjonowania, None, "Czesc systemu pozycjonowania. Potrzebuje modulu GPS.",
         "interfejs pozycjonowania"],
    75: [images.system_pozycjonowania, None, "Dzialajacy system pozycjonowania", "system pozycjonowania"],
    76: [images.nozyczki, None, "Nozyczki. Zbyt tepe, by cokolwiek przeciac. Czy mozesz je naostrzyc?",
         "tepe nozyczki"],
    77: [images.nozyczki, None, "Bardzo ostre nozyczki. Ostroznie!", "naostrzone nozyczki"],
    78: [images.moneta, None, "Mala moneta do uzycia w automatach na stacji", "moneta"],
    79: [images.karta_dostepu, None, "Ta karta dostepu nalezy do kpt. " + IMIE_GRACZA, "karta dostepu"],
    80: [images.karta_dostepu, None, "Ta karta dostepu nalezy do plk. " + IMIE_PRZYJACIELA1, "karta dostepu"],
    81: [images.karta_dostepu, None, "Ta karta dostepu nalezy do plk. " + IMIE_PRZYJACIELA2, "karta dostepu"]
}

gracz_moze_przenosic = list(range(53, 82))

#podloga, gleba, mata podlogowa, toksyczna podloga
gracz_moze_stac_na = gracz_moze_przenosic + [0, 2, 39, 48]


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
    mapa_pokoju[2][4] = 7
    mapa_pokoju[2][6] = 6
    mapa_pokoju[1][1] = 8
    mapa_pokoju[1][2] = 9
    mapa_pokoju[1][8] = 12
    mapa_pokoju[1][9] = 9
    for y in range(wys_pokoju):
        for x in range(szer_pokoju):
            obraz_do_narysowania = obiekty[mapa_pokoju[y][x]][0]
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
