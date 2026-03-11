import pygame

class Score:
	def __init__(self, x, y):
		self.value = 0
		self.x = x
		self.y = y
		self.font = pygame.font.SysFont("monospace", 35)
