import pygame
from player import Player
from constants import *
from logger import log_state

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
	player.update(dt)

	while True:
		log_state()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		updatable.update(dt)

		screen.fill("black")

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
