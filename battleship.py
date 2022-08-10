from random import randint
#set the board equal to empty list
board = []
#print O's for board spaces and make it a 5x5
for x in range(5):
  board.append(["O"] * 5)
#function to get rid of the [] chars and '' chars, will just print the O's now 
def print_board(board):
  for row in board:
    print " ".join(row)
#print the board so we can see it
print_board(board)
#need to hide the ship on a radom row
def random_row(board):
  return randint(0, len(board) - 1)
#need to hide the ship on a random column
def random_col(board):
  return randint(0, len(board[0]) - 1)
#get the random position
ship_row = random_row(board)
ship_col = random_col(board)
#uncomment for debugging purposes will tell you where the ship is hidden
#print ship_row
#print ship_col

#for loop to let the game play for 4 rounds, change as needed
for turn in range(4):
  print "Turn", turn + 1
#user to guess the row and col 
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))
#win condition 
  if guess_row == ship_row and   guess_col == ship_col:
    print "Congratulations! You sunk my battleship!"
    break
#something to handle crazy user input    
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already."
#when the user misses let them know     
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
#want to end the game after the allotted turns    
    if turn == 3:
        print "Game Over"
  
  print_board(board)
