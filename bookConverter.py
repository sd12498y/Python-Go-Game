import os.path
import sys
from state import State
from copy import deepcopy
from search import evaluate
from book import Book

alpha = 0.7
book = Book()
record_list = list()

root_dir = './Training_data/Sunday_dataset/'
for directory, subdirectories, files in os.walk(root_dir):
	for file in files:
		game = State()
		if os.path.join(file).endswith("Sunday_format.txt"):
			f = open(root_dir+file, "r")
			for line in f:
				item = line.split(',')
				player = int(item[0])
				col = int(item[1])
				row = int(item[2])
				item[3] = item[3].replace("\n","")
				result = float(item[3])
				if result == float(1):
					score = 7
				elif result == 0.5:
					score = 0
				else:
					score = -7
				#print alpha
				next = deepcopy(game)
				next.move_to(col, row, player)
				s1 = ""
				s2 = ""
				for item in game.board.flatten():
					s1 = s1 + str(item)
				for item2 in next.board.flatten():
					s2 = s2 + str(item2)
				exist = book.checkExist(game, next)
				#print exist
				if exist == None:
					alpha_init = 1
					book.book[(s1,s2)] = alpha_init*(score)
				else:
					book.book[exist] = (1-alpha) * book.book[exist] + alpha * (score)
				game.move_to(col, row, player)
			f.close()
book.save()