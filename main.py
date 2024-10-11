import pygame 
from constants import *
from circleshape import *
from player import *
def main():
    pygame.init()
    Time=pygame.time.Clock()
    dt=0
    x=SCREEN_WIDTH/2
    y=SCREEN_HEIGHT/2
    player=Player(x,y)

    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    while True:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return

       
        dt=Time.tick(60) / 1000
       
 
        player.update(dt)
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
 

    pygame.quite()
if __name__=="__main__":
    main()

