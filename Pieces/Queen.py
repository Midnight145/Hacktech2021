from Bonuses import Bonus
from Pieces import Piece
from Utils.utils import add


class Queen(Piece.Piece):
    def __init__(self, board, square, color, k: bool = None):
        super().__init__(board, square, color, "queen")
        self.bonuses = {Bonus.Knighted(): k}
        self.value = 9

    def generate_moves(self):
        moves = []
        # up right
        for i in range(1, self.board.size):
            newpos = add(self.game_pos, (i, i))
            if self.board.check_bounds(newpos):
                if self.board.get_square(newpos).has_piece and newpos != self.pos:
                    if self.can_capture(newpos):
                        moves.append(newpos)
                    break
                moves.append(newpos)

        for i in range(1, self.board.size):
            newpos = add(self.game_pos, (i, -i))
            if self.board.check_bounds(newpos):
                if self.board.get_square(newpos).has_piece and newpos != self.pos:
                    if self.can_capture(newpos):
                        moves.append(newpos)
                    break
                moves.append(newpos)

        for i in range(1, self.board.size):
            newpos = add(self.game_pos, (-i, i))
            if self.board.check_bounds(newpos):
                if self.board.get_square(newpos).has_piece and newpos != self.pos:
                    if self.can_capture(newpos):
                        moves.append(newpos)
                    break
                moves.append(newpos)

        for i in range(1, self.board.size):
            newpos = add(self.game_pos, (-i, -i))
            if self.board.check_bounds(newpos):
                if self.board.get_square(newpos).has_piece and newpos != self.pos:
                    if self.can_capture(newpos):
                        moves.append(newpos)
                    break
                moves.append(newpos)

        for i in range(self.game_pos[1], self.board.size, 1):
            newpos = add(self.game_pos, (0, i))
            if self.board.check_bounds(newpos):
                if self.board.get_square(newpos).has_piece and newpos != self.pos:
                    if self.can_capture(newpos):
                        moves.append(newpos)
                    break
                moves.append(newpos)

        # down
        for i in range(self.game_pos[1], self.board.size, 1):
            newpos = self.game_pos[0], i
            if self.board.check_bounds(newpos):
                if newpos != self.game_pos:
                    if self.board.get_square(newpos).has_piece:
                        if self.can_capture(newpos):
                            moves.append(newpos)
                        break
                    moves.append(newpos)

        # up
        for i in range(self.game_pos[1], -1, -1):
            newpos = self.game_pos[0], i

            if self.board.check_bounds(newpos):
                if newpos != self.game_pos:
                    if self.board.get_square(newpos).has_piece:
                        if self.can_capture(newpos):
                            moves.append(newpos)
                        break
                    moves.append(newpos)

        # right
        for i in range(self.game_pos[0], self.board.size, 1):
            newpos = i, self.game_pos[1]

            if self.board.check_bounds(newpos):
                if newpos != self.game_pos:
                    if self.board.get_square(newpos).has_piece:
                        if self.can_capture(newpos):
                            moves.append(newpos)
                        break
                    moves.append(newpos)

        # left
        for i in range(self.game_pos[0], -1, -1):
            newpos = i, self.game_pos[1]

            if self.board.check_bounds(newpos):
                if newpos != self.game_pos:
                    if self.board.get_square(newpos).has_piece:
                        if self.can_capture(newpos):
                            moves.append(newpos)
                        break
                    moves.append(newpos)

        tuples = []
        for key, value in self.bonuses.items():
            if value is True:
                tuples += key.tuples
        for i in tuples:
            i = add(self.game_pos, i)
            if self.board.check_bounds(i):
                if self.board.get_square(i).has_piece and i != self.game_pos:
                    if self.can_capture_(i):
                        moves.append(i)
                else:
                    moves.append(i)

        return moves
