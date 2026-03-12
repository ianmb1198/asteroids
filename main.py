import pygame
import sys
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from lives import Lives
from constants import *
from logger import log_state, log_event
from score import Score

def main():
	#Print basic game info to the console on startup.
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

	#Initialize all imported pygame modules.
	pygame.init()

	#Create the game window and the internal clock for managing framerate.
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	#Delta time (dt) tracks the time passed between frames for smooth movement.
	dt = 0

	#Groups allow us to update or draw multiple objects at once.
	updatable = pygame.sprite.Group()	#For movement and logic.
	drawable = pygame.sprite.Group()	#For rendering to the screen.

	#Assign groups to class containers so new objects add themselves automatically.
	Player.containers = (updatable, drawable)
	player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT /2)

	#Setup asteroid groups and the manager that spans them.
	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()

	#Setup shot (bullet) groups and containers.
	shots = pygame.sprite.Group()
	Shot.containers = (shots, updatable, drawable)

	#Initialize the UI for tracking and displaying the score.
	score_keeper = Score(10, 10)
	total_points = 0

	#Initialize the UI for tracking and displaying the total lives the player has.
	life_manager = Lives(3, 10, 50)	#Starting with 3 lives, positioned below score.

	#--- Game Loop ---#
	while True:
		#Log the current game state for debugging.
		log_state()

		#Check for window events (like clicking the "X" to close).
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		#Move and update all objects based on the time passed (dt)
		updatable.update(dt)

		#Collision Check: Asteroid vs Player.
		for asteroid in asteroids:
			if asteroid.collides_with(player):
				log_event("player_hit")
				#Respawn logic: reset player to center
				if life_manager.decrease():
					player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
					player.velocity = pygame.Vector2(0, 0)
					#Clear nearby asteroids to prevent instant death upon reset.
					for a in asteroids:
						if a.position.distance_to(player.position) < 200:
							a.kill()
				else:
					print("Game over!")
					print(f"Score: {total_points}")
					sys.exit()

		#Collision Check: Asteroid vs Shot (Bullets)
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collides_with(shot):
					log_event("asteroid_shot")
					points = 100 if asteroid.radius > ASTEROID_MIN_RADIUS else 250
					score_keeper.increment(points)
					total_points += points
					asteroid.split()
					shot.kill()

		##--- Rendering Section ---##
		screen.fill("black")	#Clear the screen with black.

		#Draw every object in the drawable group.
		for obj in drawable:
			obj.draw(screen)

		#Draw the score overlay.
		score_keeper.draw(screen)

		#Draw the life overlay.
		life_manager.draw(screen)

		#Update the actual display monitor.
		pygame.display.flip()

		#Limit framerate to 60 FPS and calculate delta time (dt)
		dt = clock.tick(60) / 1000

#Entry point check
if __name__ == "__main__":
    main()
