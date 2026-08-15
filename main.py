import pygame
import sys
import player
import asteroid
import asteroidfield
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfields = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_ship = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield.AsteroidField()



    while(True):
        log_state()

        # to start processing event queue and to keep program responsive
        for event in pygame.event.get():
            pass

        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

        for ast in asteroids:
            if ast.collides_with(player_ship):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return     

if __name__ == "__main__":
    main()
