
import random
import math

class Player:
  def __init__(self, letter) -> None:
    self.letter = letter
  
  def get_move(self, board):
    pass

class RandomComputerPlayer(Player):
  
  def __init__(self, letter) -> None:
    super().__init__(letter)
  
  def get_move(self, board):
    return random.choice(board.available_moves())

class HumanPlayer(Player):
  def __init__(self, letter) -> None:
    super().__init__(letter)
  
  def get_move(self, board):
    valid_moves = board.available_moves()
    is_valid = False
    val=None
    while not is_valid:
      square = input(self.letter +"'s turn. Type your move as rc, r= row and c=column: ")
      try:
        row = int(square[0])
        column = int(square[1])
        val = board.size*row +column

        if val not in valid_moves:
          raise ValueError
        else: 
          is_valid = True
      except:
        print('Not a valid move. Try again')
      
    return val


class ComputerHardPlayer(Player):
  def __init__(self, letter) -> None:
    super().__init__(letter)
  
  def get_move(self, game):
    valid_moves = game.available_moves()
    if len(valid_moves) == game.size**2:
      square = random.choice(valid_moves)
    else:
      square = self.minimax(game, self.letter)['position']
    return square

  def minimax(self, game, player):
    max_player = self.letter
    other_player = "X" if player == 'O' else 'O'
    empty_squares = game.available_moves()
    num_empty_squares = len(empty_squares)
    winner = game.winner
    if game.winner == other_player: 
      return {'position': None,
              'score': 1*(num_empty_squares+1) if max_player == other_player else -1*(num_empty_squares+1)
              }
    elif num_empty_squares == 0: 
      return {'position': None, 'score': 0}
    
    if max_player == player:
      best = {'position': None, 'score': -math.inf}
    else:
      best = {'position':None, 'score': math.inf}
    
    for move in empty_squares:
      #try move
      
      game.make_move(move,player, blind = True)
      #simulate a game after that move through minmax
      sim_score = self.minimax(game, other_player)

      #undo move
      game.board[move] = ' '
      game.winner = winner
      sim_score['position'] = move
      
      #update best
      if player == max_player:
        if sim_score['score'] > best['score']:
          best = sim_score
      else:
        if sim_score['score'] < best['score']:
          best = sim_score
    return best