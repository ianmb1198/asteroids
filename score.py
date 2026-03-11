import pygame

class Score:
	def __init__(self, x, y):
		self.value = 0
		self.x = x
		self.y = y
		self.font = pygame.font.SysFont("monospace", 35)

	#Method to increment score.
	def increment(self, points):
		self.value += points

	#Method to draw a score surface on the main screen.
	def draw(self, screen):
		#Render creates a new Surface with the text on it.
		score_surface = self.font.render(f"Score: {self.value}", True, (255, 255, 255))

		#Blit draws that surface on the main screen.
		screen.blit(score_surface, (self.x, self.y))
