import pygame 
from constants import *
from circleshape import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init()
    Time=pygame.time.Clock()
    dt=0
    x=SCREEN_WIDTH/2
    y=SCREEN_HEIGHT/2
   
    updateable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    Player.containers=(updateable,drawable)
    
    
    asteroids = pygame.sprite.Group()
    
    
    AsteroidField.containers = (updateable,)
    Asteroid.containers = (asteroids, updateable, drawable)
    player=Player(x,y)
    asteroid_field=AsteroidField()
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    while True:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return

       
        dt=Time.tick(60) / 1000
       
        for updateable_object in updateable:
            updateable_object.update(dt)

        

        screen.fill((0,0,0))
        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()
 

    pygame.quit()
if __name__=="__main__":
    main()

