import math
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def tileAt(rect, filename, colorkey = None):
    rect = pygame.Rect(rect)
    image = pygame.Surface(rect.size).convert()
    image.blit(pygame.image.load(filename).convert_alpha(), (0, 0), rect)
    return image

def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True
    return False

def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False

class Position(object):
    """
    A Position represents a location in a two-dimensional space.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y      
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position with the
        specified angle and speed.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.x, self.y
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(int(round(new_x)), int(round(new_y)))

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)
