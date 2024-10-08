import pygame 
from constants import *
from circleshape import *
def main():
    pygame.init()
    Time=pygame.time.Clock()
    dt=0
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return

        screen.fill((0,0,0))
        pygame.display.flip()
        
        dt=Time.tick(60) / 1000
if __name__=="__main__":
    main()

