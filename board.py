import pygame

class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        self.grid = [[0 for _ in range(board_size[0])] for _ in range (board_size[1])]
        self.colors = [[(0, 0, 0) for _ in range(board_size[0])] for _ in range(board_size[1])]

    def display(self, screen):
        for y in range(self.board_size[1]):
            for x in range(self.board_size[0]):
                if self.grid[y][x] != 0:
                    pygame.draw.rect(screen, self.colors[y][x],
                                     (x * self.board_size[2] + 40, 60 + y * self.board_size[2],
                                      self.board_size[2], self.board_size[2]))

    def add_shape_to_board(self, player):
        for (x,y) in player.get_shape_positions():
            self.grid[y][x] = 1
            self.colors[y][x] = player.color

    def is_collision(self, player):
        for(x, y) in player.get_shape_positions():
            if x < 0 or x >= self.board_size[0] or y >= self.board_size[1] or self.grid[y][x] != 0:
                return True
            return False

    def clear_lines(self):
        lines_cleared = 0
        for y in range(self.board_size[1]):
            if 0 not in self.grid[y]:
                del self.grid[y]
                del self.colors[y]
                self.grid.insert(0, [0 for _ in range(self.board_size[0])])
                self.colors.insert(0, [(0, 0, 0) for _ in range(self.board_size[0])])
                lines_cleared += 1
                return lines_cleared
