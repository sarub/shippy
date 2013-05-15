import pygame
from ships import *
from levels import *
from util import *

class Game:
    def __init__(self, ship, level):
        #Screen init
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", 15)
        self.ship = ship
        self.level = level

        self.run()

    def run(self):
        run = True
        pause = False
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = not pause

            if not pause:
                #Player actions
                if pygame.key.get_pressed()[pygame.K_UP]:
                    self.ship.move(180)
                elif pygame.key.get_pressed()[pygame.K_DOWN]:
                    self.ship.move(0)

                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    self.ship.move(270)
                elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                    self.ship.move(90)

                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    self.ship.fireWeapon(ship.weapon_main)

                if pygame.key.get_pressed()[pygame.K_LCTRL]:
                    self.ship.fireWeapon(ship.weapon_sec)

                #Check collisions
                for enemy in self.level.spammed_enemys:
                    for projectile in self.ship.projectiles:
                        if doRectsOverlap(
                            projectile.image.get_rect().move(projectile.position.x, projectile.position.y),
                            enemy.image.get_rect().move(enemy.position.x, enemy.position.y)):
                            projectile.collision(enemy)

                #Update
                self.clock.tick(60)
                self.ship.tick()
                self.level.tick()


            #Draw screen
            self.draw()

            if pause:
                s = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
                s.fill((0, 0, 0, 128))
                s.blit(self.font.render("Pause", 40, (255, 255, 255)), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
                screen.blit(s, (0,0))

            pygame.display.flip()

    def draw(self):
        #background
        self.level.draw(screen)

        #ships
        screen.blit(self.ship.image, (self.ship.position.x, self.ship.position.y))
        for ship in self.level.spammed_enemys:
            screen.blit(ship.image, (ship.position.x, ship.position.y)) 

        #Projectiles
        for projectile in self.ship.projectiles:
            screen.blit(projectile.image, (projectile.position.x, projectile.position.y)) 

        #HUD
        screen.blit(self.font.render("Energy: " + str(self.ship.generator.energy), 1, (255, 255, 255)), (650, 10))
        screen.blit(self.font.render("Shields: " + str(self.ship.shield.energy), 1, (255, 255, 255)), (650, 30))
        screen.blit(self.font.render("Hull: " + str(self.ship.hull), 1, (255, 255, 255)), (650, 50))
        screen.blit(self.font.render("Score: " + str(self.ship.score), 1, (255, 255, 255)), (650, 70))


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ship = Ship(Position(400, 500))
level = Level("level_0")
game = Game(ship, level)

