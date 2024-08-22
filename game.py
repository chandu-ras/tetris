import pygame
from player import Player
from board import Board

class Game :
    def __init__(self, board_size, screen):
        self.board = Board(board_size)
        self.player = Player(board_size, screen)
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.done = False
        self.drop_speed = 500
        self.last_drop_time = pygame.time.get_ticks()
        self.score = 0

    def run(self):
        while not self.done:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(30)

    def handle_events(self):
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player.move(-1, 0)
                if self.board.is_collision(self.player):
                    self.player.move(1,0)
            elif event.key == pygame.K_RIGHT:
                self.player.move(1, 0)
                if self.board.is_collision(self.player):
                    self.player.move(-1, 0)
            elif event.key == pygame.K_DOWN:
                self.player.move(0, 1)
                if self.board.is_collision(self.player):
                    self.player.move(0, -1)
                    self.lock_piece()
            elif event.key == pygame.K_UP:
                self.player.rotate()
                if self.board.is_collision(self.player):
                    self.player.rotate()
                    self.player.rotate()
                    self.player.rotate()

    def update(self):
        if pygame.time.get_ticks() - self.last_drop_time > self.drop_speed:
            self.player.move(0, 1)
        if self.board.is_collision(self.player):
               self.player.move(0, -1)
               self.lock_piece()
               self.last_drop_time = pygame.time.get_ticks()

    def lock_piece(self):
         self.board.add_shape_to_board(self.player)
         self.board.clear_lines()
         self.player.reset()
         if self.board.is_collision(self.player):
             self.done = True


    def render(self):
        self.screen.fill((220,220,220))
        self.board.display(self.screen)
        self.player.display()
        self.draw_grid()
        pygame.display.flip()

    def draw_grid(self):
        for i in range(self.board.board_size[1]):
            for j in range(self.board.board_size[0]):
                pygame.draw.rect(self.screen, (200, 160, 10),
                                 (j * self.board.board_size[2] + 40, 60 + i * self.board.board_size[2],
                                  self.board.board_size[2], self.board.board_size[2]), 1)






