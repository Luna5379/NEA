import pygame
import sys
import sqlite3

#start it all over from the beginning
pygame.init()

def events():
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == 