import pygame
pygame.init() #Initiates pygame    
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
PURPLE = (255,0,255)
BLUE = (0,0,255)
WHITE = (255,255,255)
YELLOW = (255,255,0)
xSize,ySize = 640,480 #Sets size of window
screen = pygame.display.set_mode((xSize,ySize),pygame.RESIZABLE) #creates main surface
screenFlipped = pygame.display.set_mode((xSize,ySize),pygame.RESIZABLE) #creates surface that will be flipped (mirror display)
screen.fill(BLACK) #Make the window black
print "Initiated"
pygame.draw.line(screen, (0, 0, 255), (0, 0), (639, 479))
