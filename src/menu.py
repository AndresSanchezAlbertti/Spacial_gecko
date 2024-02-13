import pygame
from configuraciones import*
from class_boton import *

NEGRO= (0, 0, 0)

button_surface = pygame.image.load("menu/0.png")
button_surface = pygame.transform.scale(button_surface, (400, 150))

button = Button(button_surface, 400, 300, "Button")

while True:
	pygame.init()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			button.checkForInput(pygame.mouse.get_pos())

	PANTALLA.fill("white")

	button.update()
	button.changeColor(pygame.mouse.get_pos())

	pygame.display.update()