import pygame

class Lives:
	def __init__(self, count, x, y):
		self.amount = count
		self.x = x
		self.y = y
		self.font = pygame.font.SysFont("monospace", 35)

	def decrease(self):
		self.amount -= 1
		return self.amount > 0

	def draw(self, screen):
		lives_surface = self.font.render(f"Lives: {self.amount}", True, (255, 255, 255))
		screen.blit(lives_surface, (self.x, self.y))
