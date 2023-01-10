class TicTacToe:
    def __init__(self,board):
        self.board = self.make_board()
        self.winner = None

    @staticmethod
    def make_board(self):
        return[' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print(' |' +' | '.join(row)+' |')

            

        
