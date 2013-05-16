import pygame
from ships import *
from levels import *
from util import *

class Game:
    def __init__(self, ship, level):
        """
        Game init
        """
        #Screen init
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", 15)
        self.ship = ship
        self.level = level

        self.run()

    def run(self):
        """
        Main logic
        """
        run = True
        pause = False
        dead = False
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = not pause

            if (not pause) and (not dead):
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
                self.collisions()
                
                if self.ship.hull <= 0.0:
                    dead = True

                #Update
                self.clock.tick(60)
                self.ship.tick()
                self.level.tick()

            #Draw screen
            self.draw()

            if pause or dead:
                if pause:
                    text = pygame.font.SysFont("monospace", 40).render("Pause", True, (255, 255, 255))
                else:
                    text = pygame.font.SysFont("monospace", 40).render("Game over!", True, (255, 255, 255))

                popup = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
                popup.fill((0, 0, 0, 128))
                popup.blit(text, ((SCREEN_WIDTH / 2) - (text.get_width() / 2), (SCREEN_HEIGHT / 2) - (text.get_height() / 2)))
                screen.blit(popup, (0, 0))

            pygame.display.flip()


    def collisions(self):
        """
        Checks for collisions and projectile impacts
        """
        for enemy in self.level.spammed_enemys:
            if doRectsOverlap(
                    self.ship.image.get_rect().move( self.ship.position.x,  self.ship.position.y),
                    enemy.image.get_rect().move(enemy.position.x, enemy.position.y)):
                self.ship.impact(50.0)
                enemy.impact(75.0)
                self.ship.move(90, 10.0)
                       

            for projectile in self.level.projectiles:
                if projectile.owner == self.ship and doRectsOverlap(
                    projectile.image.get_rect().move(projectile.position.x, projectile.position.y),
                    enemy.image.get_rect().move(enemy.position.x, enemy.position.y)):
                    projectile.collision(enemy)
            
        #enemy projectiles vs self
        for projectile in self.level.projectiles:
            if projectile.owner != self.ship and doRectsOverlap(
                projectile.image.get_rect().move(projectile.position.x, projectile.position.y),
                self.ship.image.get_rect().move(self.ship.position.x, self.ship.position.y)):
                projectile.collision(self.ship)

    def draw(self):
        """
        Draws everything
        """
        #background
        self.level.draw(screen)

        #ships
        screen.blit(self.ship.image, (self.ship.position.x, self.ship.position.y))
        for ship in self.level.spammed_enemys:
            screen.blit(ship.image, (ship.position.x, ship.position.y)) 

        #Projectiles
        for projectile in level.projectiles:
            screen.blit(projectile.image, (projectile.position.x, projectile.position.y)) 
        
        #HUD
        screen.blit(self.font.render("Energy: " + str(self.ship.generator.energy), True, (255, 255, 255)), (650, 10))
        screen.blit(self.font.render("Shields: " + str(self.ship.shield.energy), True, (255, 255, 255)), (650, 30))
        screen.blit(self.font.render("Hull: " + str(self.ship.hull), True, (255, 255, 255)), (650, 50))
        screen.blit(self.font.render("Score: " + str(self.ship.score), True, (255, 255, 255)), (650, 70))


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
level = Level("level_0")
ship = Ship(Position(400, 500), level)

game = Game(ship, level)

