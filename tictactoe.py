import random
from time import sleep
#from pcstrat.py import unbeatable

def main():
  #get mode of play for o
  o_mode = int(input(""" Select first player:
  1. Human
  2. PC
  """))
  #get mode of play for x
  x_mode = int(input(""" Select second player:
  1. Human
  2. PC
  """))
  #initialize (decide size of) board
  size = 3
  rows = range(size)
  cols = range(size)
  board = [[f'{j}{i}' for i in cols] for j in rows]
  show_game(board)
  i=0
  while i < size**2 /2 :
    make_move(board, o_mode,'O')
    show_game(board)
    print(' ')
    sleep(1)
    make_move(board, x_mode, 'X')
    show_game(board)
    print(' ')
    i+=1

def show_game(board):
  for i in range(3):
   print(' | '.join(board[i]))

def get_pos(board, letter):
  pos = []
  return
  
def make_move(board, mode, turn):
  x_array = get_pos(board,'X')
  o_array = get_pos(board,'O')
  if mode == 1:
    move = input("Make your move: ")
    board[int(move[0])][int(move[1])] = turn+' '
  #else:
  

if __name__ == '__main__':
  main()
