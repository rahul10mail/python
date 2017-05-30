import pygame

pygame.display.init()
canvas = pygame.display.set_mode((480, 480))

r = 0
g = 0
b = 0

while r < 255:
	color = (r, g, b)
	canvas.fill(color)
	pygame.display.update()
	r += 1
	g += 1
	b += 1
	
	r %= 127
	g %= 255
	b %= 127
