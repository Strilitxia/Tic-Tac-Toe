# SPDX-FileCopyrightText: 2025-2026 Asif Amin 
# SPDX-License-Identifier: MIT

import pygame

#initialize pygame
pygame.init()


#screen dimension
HEIGHT,WIDTH=550,600


#colors


#initialize screen
screen=pygame.display.set_mode((HEIGHT,WIDTH))



#game title and logo
pygame.display.set_caption("Tic-Tac-Toe")



screen_condition=True
while screen_condition:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         screen_condition = False
