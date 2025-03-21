import pygame

pygame.init()


screen=pygame.display.set_mode((550,600))



#game title and logo
pygame.display.set_caption("Tic-Tac-Toe")


#initialize screen
screen_condition=True
while screen_condition:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         screen_condition = False