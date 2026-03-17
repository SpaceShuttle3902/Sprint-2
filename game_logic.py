class PegSolitaireGame:

    def __init__(self, size=7):
        self.size = size
        self.board_type = "English"
        self.initialize_board()

    def initialize_board(self):

        self.board = [[1]*self.size for _ in range(self.size)]

        center = self.size // 2
        self.board[center][center] = 0


    def make_move(self,r1,c1,r2,c2):

        rm = (r1+r2)//2
        cm = (c1+c2)//2

        if r2 < 0 or r2 >= self.size:
            return False
        if c2 < 0 or c2 >= self.size:
            return False

        if abs(r1-r2)==2 and c1==c2 or abs(c1-c2)==2 and r1==c2:

            if self.board[r1][c1]==1 and self.board[rm][cm]==1 and self.board[r2][c2]==0:

                self.board[r1][c1]=0
                self.board[rm][cm]=0
                self.board[r2][c2]=1

                return True

        return False


    def is_game_over(self):

        directions = [
            (0, 2),
            (0, -2),
            (2, 0),
            (-2, 0)
        ]

        for r in range(self.size):
            for c in range(self.size):

                if self.board[r][c] != 1:
                    continue

                for dr, dc in directions:

                    r2 = r + dr
                    c2 = c + dc
                    rm = r + dr//2
                    cm = c + dc//2

                    if 0 <= r2 < self.size and 0 <= c2 < self.size:
                        if self.board[rm][cm] == 1 and self.board[r2][c2] == 0:
                            return False

        return True