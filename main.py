import pygame
from game import Game

pygame.init()

size = (400, 500)
board_size = (10, 20, 20)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tetris')

game = Game(board_size, screen)
game.run()

pygame.quit()