import pygame
import sys
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from constants import *
from logger import log_state, log_event

def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT /2)

	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)

	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()

	#Set up new shots group and the containers field to include the group with drawable and updateble containers.
	shots = pygame.sprite.Group()
	Shot.containers = (shots, updatable, drawable)

	#Game Loop
	while True:
		log_state()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		updatable.update(dt)

		#Collision check
		for asteroid in asteroids:
			if asteroid.collides_with(player):
				log_event("player_hit")
				print("Game over!")
				sys.exit()

		#Second collision check
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collides_with(shot):
					log_event("asteroid_shot")
					asteroid.split()
					shot.kill()

		screen.fill("black")

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
