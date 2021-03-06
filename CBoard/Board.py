import pygame

from CBoard import Square


class Board:
    def __init__(self, size: int):
        self.size = size
        self.board = [[] for i in range(size)]
        self.board_rects = []
        self.board_sprites = pygame.sprite.Group()
        self.white_pieces = pygame.sprite.Group()
        self.black_pieces = pygame.sprite.Group()
        self.screen = None
        self.boardState = 0

    def create_board(self) -> pygame.Surface:
        self.screen = pygame.display.set_mode(
            (self.size * 8 * 10, self.size * 8 * 10))

        flag = False
        current_coords = [0, 0]
        color = (80, 80, 80)
        for i in range(self.size):
            for k in range(self.size):
                if flag:
                    self.board[i].append(Square.Square(
                        (current_coords[0], current_coords[1]), color, self.size))
                else:
                    self.board[i].append(Square.Square(
                        (current_coords[0], current_coords[1]), (0, 0, 0), self.size))
                current_coords[0] += 80
                if current_coords[0] >= self.size * 8 * 10:
                    current_coords[1] += 80
                    current_coords[0] = 0
                    flag = not flag
                if current_coords[1] >= self.size * 8 * 10:
                    current_coords[0] += 80
                    current_coords[1] = 0
                    flag = not flag
                flag = not flag

        return self.screen

    def get_square(self, pos: tuple) -> Square.Square:
        return self.board[pos[1]][pos[0]]

    def get_rect(self, pos: tuple):
        return self.board_rects[self.size * pos[0] + pos[1]]

    def check_bounds(self, pos: tuple) -> bool:
        return 0 <= pos[0] < self.size and 0 <= pos[1] < self.size

    def get_enemy_pieces(self, color):
        if color:
            return self.black_pieces
        return self.white_pieces

    def get_point_value(self, color):
        return sum([i.value for i in (self.white_pieces if color else self.black_pieces)])

    def calculate_value(self):
        return 40 + self.get_point_value(False) - self.get_point_value(True)
