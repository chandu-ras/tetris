import pygame
import random


# class Player:


class Player:
    shapes = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],  # I SHAPE
        [[4, 5, 9, 10], [2, 6, 5, 9]],  # Z SHAPE
        [[6, 7, 9, 10], [1, 5, 6, 10]],  # S SHAPE
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],  # L SHAPE
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  # UMGEDREHTES L
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],  # HAT / UPPER HALF PLUS
        [[1, 2, 5, 6]],  # Square
    ]

    colors = [
        (20, 203, 12),  # GRÜN
        (203, 20, 12),  # ROT
        (20, 12, 203),  # BLAU
        (203, 203, 12),  # GELB
        (12, 203, 203),  # CYAN
        (203, 12, 203),  # MAGENTA
        (203, 100, 12),  # ORANGE
    ]

    def __init__(self, board_size, screen):
        self.screen = screen
        self.board_size = board_size
        self.x_position = board_size[0] // 2 - 2  # Initial in der Mitte
        self.y_position = 0
        self.shape_index = random.randint(0, len(self.shapes) - 1)
        self.rotation = 0
        self.shape = self.shapes[self.shape_index]
        self.color = self.colors[self.shape_index]

    def display(self):
        for i in range(4):
            for j in range(4):
                if (i * 4 + j) in self.shape[self.rotation]:
                    pygame.draw.rect(self.screen, self.color,
                                     (self.x_position * self.board_size[2] + j * self.board_size[2]
                                      + 40, 60 + (self.y_position + i) * self.board_size[2],
                                      self.board_size[2], self.board_size[2]))

    def rotate(self):
        # rotiert die Form
        self.rotation = (self.rotation + 1) % len(self.shape)

    def move(self, dx, dy):
        # Bewegt die Figur
        self.x_position += dx
        self.y_position -= dy

    def get_shape_positions(self):
        positions = []
        for i in range(4):
            for j in range(4):
                if (i * 4 + j) in self.shape[self.rotation]:
                    positions.append((self.x_position + j, self.y_position + i))
        return positions

    def reset(self):
        # Setzt azf die Anfngsposition zurück und wählt eine neue zufällige Form
        self.x_position = self.board_size[0] // 2 - 2
        self.y_position = 0
        self.shape_index = random.randint(0, len(self.shapes) - 1)
        self.rotation = 0
        self.shape = self.shapes[self.shape_index]
        self.color = self.colors[self.shape_index]
