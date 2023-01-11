class TicTacToe:
    #the init method has the ttt board function that diplays it virtually and also the winner of the match
    def __init__(self,board):
        self.board = self.make_board()
        self.winner = None
   #since we do not need the class or instance variables so this function is static 
    @staticmethod
    def make_board():
        return[' ' for _ in range(9)]

    # 
    def print_board(self):
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print(' |' +' | '.join(row)+' |')

    #first we 
    @staticmethod
    def print_board_nums():
        number_board = [str(i) for i in range(j*3 ,(j+1)*3) for j in range(3)] # 1 2 3 4 5 6 7 8 9 these are all strings
        for row in number_board:
            print('| '+' | '.join(row)+' |')
            #row is the ith row number
   
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
            return len(self.available_moves())



    def available_moves(self):
        moves = []
        for (i,move) in enumerate(self.board):
            if move == " ":
                moves.append(i)
        return moves         
     #the print_game is for when the computer plays against computer so we do not need to watch the entire game 

    def make_move(self,square,letter):
        if self.board == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False     
            


def play(game,x_player,o_player,print_game = True):

    if print_game:
        return print_board_nums()

    letter = 'X'    

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)   

    if game.make_move(square,letter):
        if print_game:
            print(f'{letter} makes a move at {square}')
            game.print_board
            print(' ')

    if game.current_winner :
        if print_game:
            print(letter + ' wins the match!')
        return letter   

    letter = 'O' if letter == 'X' else  'X'        
if print_game:
    print('It\'s a Tie!')
            


#why is there a print borad and a print borad nums both when only the latter is used 