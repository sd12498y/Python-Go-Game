import random
from board import Board
from state import State
from search import min_max_search, alpha_beta_search
from Tkinter  import * 
import numpy as np

#computer_white or computer_black or human	
black = sys.argv[1]
white = sys.argv[2]
if black=='human' or white=='human':
	root = State()	
	board = Board(root, black, white, round)
elif black=='SQ' or white=="SQ":
	round = sys.argv[3]
	root = State()	
	board = Board(root, black, white, round)



