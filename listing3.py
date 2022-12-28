mapa_pokoju = [ [1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1]
                ]


WIDTH = 800
HEIGTH = 800

gora_lewa_x = 100
gora_lewa_y = 150

OBIEKTY_DEMO = [images.podloga, images.filar]

wys_pokoju = 7
szer_pokoju = 5

def draw():
    for y in range(wys_pokoju):
        for x in range(szer_pokoju):
            obraz_do_narysowania = OBIEKTY_DEMO[mapa_pokoju[y][x]]
            screen.blit(obraz_do_narysowania,
                        (gora_lewa_x+(x*30),
                        gora_lewa_y+(y*30) - obraz_do_narysowania.get_height()))
