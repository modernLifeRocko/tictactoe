from player import HumanPlayer, RandomComputerPlayer, ComputerHardPlayer

class TicTacToe:
  def __init__(self, size = 3) -> None:
    self.size = size
    self.board = [' ' for i in range(size**2)]
    self.winner = None
  
  def print_board(self):
    print(' | '+' | '.join([f"{i}" for i in range(self.size)])+' |')
    for r, row in enumerate([self.board[i*self.size:(i+1)*self.size] for i in range(self.size) ]):
      print(f'{r}| '+ ' | '.join(row)+' |')
  
  def available_moves(self):
    return [i for i, spot in enumerate(self.board) if spot == ' ']

  def is_winner_move(self, square, letter):
    #check row
    rowi = square // self.size
    row = self.board[rowi*self.size:(rowi+1)*self.size]
    if all([spot == letter for spot in row]):
      return True
    #check column
    coli = square % self.size
    col = self.board[coli:1+coli+self.size*(self.size-1):self.size]
    if all([spot == letter for spot in col]):
      return True
    #check diagonals
    diag = self.board[0:self.size**2:self.size+1]
    if all([spot == letter for spot in diag]):
      return True
    antidiag = self.board[self.size-1: self.size*(self.size-1)+1: self.size-1]
    if all([spot == letter for spot in antidiag]):
      return True
    return False

  def make_move(self, square, letter, blind = False):
    if self.board[square] == ' ':
      self.board[square] = letter
    
    if not blind:
      print(" ")
      self.print_board()
    if self.is_winner_move(square, letter):
      self.winner = letter
      return True
    return False

def play(game,x_player, o_player, starting_letter='O', blind=False):
  if not blind:
    #shows starting grid with their coordinates
    game.print_board()
  letters = ['O', 'X']
  players = [o_player, x_player]
  turn = letters.index(starting_letter)
  round = 0
  while " " in game.board:
    #player in turn moves
    move = players[turn].get_move(game)
    game.make_move(move,letters[turn])
    print(round)
    round +=1
    #check win
    if game.is_winner_move(move, letters[turn]):
      print (f"{letters[turn]} won. ")
      return  1
    
    #update turn
    turn = (turn + 1) % 2
  print("A kravate? It's a tie") 
if __name__ == '__main__':
  mode1 = int(input("""O player mode:
  1. Manual
  2. Random
  3. PC"""))
  mode2 = int(input("""X player mode:
  1. Manual
  2. Random
  3. PC"""))
  
  if mode1 == 1:
      x_player = HumanPlayer('X')
  elif mode1 == 2:
      x_player = RandomComputerPlayer('X')
  else:
      x_player= ComputerHardPlayer('X')
  
  if mode2 == 1:
      o_player= HumanPlayer('O')
  elif mode2 == 2: 
      o_player = RandomComputerPlayer('O')
  else :
      o_player = ComputerHardPlayer('O')
    
  t = TicTacToe(size = 4)
  play(t, x_player, o_player, starting_letter = 'O')
