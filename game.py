import pygame
from ships import *
from levels import *
from util import *


#Screen init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 15)

def run():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #Player actions
        if pygame.key.get_pressed()[pygame.K_UP]:
            ship.move(180)
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            ship.move(0)

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            ship.move(270)
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            ship.move(90)

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            ship.fireWeapon(ship.weapon_main)

        #Check collisions

        #Draw screen
        draw()
        pygame.display.flip()

        #Update
        clock.tick(30)
        ship.tick(1)
        level.tick(1)


def draw():
    #background
    screen.fill((0, 0, 0))
    screen.blit(level.background, (0, 0))

    #ships
    screen.blit(ship.image, (ship.position.x, ship.position.y))

    #Projectiles
    for projectile in ship.projectiles:
        pygame.draw.circle(screen, (255, 0 , 0), (projectile.position.x, projectile.position.y), 1, 1)

    #HUD
    screen.blit(font.render("Energy: " + str(ship.generator.energy), 1, (255, 255, 255)), (650, 10))
    screen.blit(font.render("Shields: " + str(ship.shield.energy), 1, (255, 255, 255)), (650, 30))
    screen.blit(font.render("Hull: " + str(ship.hull), 1, (255, 255, 255)), (650, 50))

ship = Ship(Position(400, 500))
level = Level()
run()
