import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (bullets, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # backup previous player position
        player_pos = player.position.copy()

        updatable.update(dt)

        # prevent player out from screen
        if not player.is_inside(screen):
            print("player not inside")
            player.position = player_pos

        # kill bullet outside screen
        for bullet in bullets:
            if bullet.is_outside(screen):
                bullet.kill()

        for asteroid in asteroids:
            if asteroid.is_collide(player):
                print("Game over!")
                sys.exit()
            if asteroid.is_outside(screen):
                asteroid.kill()
                continue
            for bullet in bullets:
                if asteroid.is_collide(bullet):
                    bullet.kill()
                    asteroid.split()

        # print(f"bullet: {len(bullets)} , asteroid: {len(asteroids)}")
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()