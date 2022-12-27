WIDTH = 800
HEIGHT = 600
gracz_x = 600
gracz_y = 350


def draw():
    screen.blit(images.tlo, (0, 0))
    screen.blit(images.mars, (50, 50))
    screen.blit(images.astronauta, (gracz_x, gracz_y))
    screen.blit(images.statek, (130, 150))


def petla_gry():
    global gracz_x, gracz_y
    if keyboard.right:
        gracz_x += 5
    if keyboard.left:
        gracz_x -= 5
    if keyboard.up:
        gracz_y -= 5
    if keyboard.down:
        gracz_y += 5


clock.schedule_interval(petla_gry, 0.03)
