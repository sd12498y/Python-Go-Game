from Tkinter  import * 
import numpy as np
from copy import deepcopy
from search import min_max_search, alpha_beta_search
from SQagent import SQagent
from book import Book
from state import State
class Board():
	
	def __init__(self, state, black, white, *round):
		self.state = state
		self.root     =  Tk()
		self.canvas   =  self.setUpCanvas()
		self.setUpInitialBoard()
		if black=="human":
			self.root.bind('<Button-1>', self.click_black) # 1 = LEFT  mouse button.
			self.root.bind('<Button-3>', self.click_black) # 3 = RIGHT mouse button.
		elif white=="human":
			self.root.bind('<Button-1>', self.click_white) # 1 = LEFT  mouse button.
			self.root.bind('<Button-3>', self.click_white) # 3 = RIGHT mouse button.
			self.computerMove(1)
		if black=="SQ":
			self.loop("black", round[0])
		elif white=="SQ":
			self.loop("white", round[0])
		self.root.mainloop()
		'''
		for i in range(64):
			if i==27 or i == 36:
				self.board = self.board + "w"
			elif i==28 or i==35:
				self.board = self.board + "b"
			else:
				self.board = self.board + "-"
		self.board = list(self.board)'''

	def displayUI(self):
		for r in range (8):
			for c in range (8):
				if self.state.board[r][c] == 1:
					sx = c*70 + 85
					sy = r*70 + 105
					self.canvas.create_oval(sx-25,sy-25, sx+25, sy+25, fill = 'BLACK')
				if self.state.board[r][c] == -1:
					sx = c*70 + 85
					sy = r*70 + 105
					self.canvas.create_oval(sx-25,sy-25, sx+25, sy+25, fill = 'WHITE')
		self.canvas.update()

	def setUpCanvas(self): # These are the REQUIRED magic lines to enter graphics mode.
		self.root.title("Othello") # Your screen size may be different from 1270 x 780.
		canvas = Canvas(self.root, width = 900, height = 780, bg = 'GREY30')
		canvas.pack(expand = YES, fill = BOTH)
		return canvas

	def setUpInitialBoard(self):

	 	#print title
		self.canvas.create_text(330, 50, text = "OTHELLO with AI", \
							 fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))

	 	#draw outer box, with brown border
		self.canvas.create_rectangle(50, 70, 610, 630, width = 5, fill    = 'DARKGREEN', outline = 'BROWN')

	 	#Draw 7 horizontal and 7 vertical lines to make the cells
		for n in range (1, 8): # draw horizontal lines
			 self.canvas.create_line(50, 70+70*n, 610, 70+70*n, width = 2, fill = 'BLACK')
		for n in range (1, 8):# draw vertical lines
			 self.canvas.create_line(50+70*n,  70, 50+70*n, 630, width = 2, fill = 'BLACK')


	 	#Place a to h at bottom
		tab = " " * 11
		stng = 'a' + tab + 'b' + tab + 'c' + tab + 'd' + tab + 'e' + \
					 tab + 'f' + tab + 'g' + tab + 'h'
		self.canvas.create_text(325, 647, text = stng, fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))

	 	#Place letters on left side
		for n in range (0,8):
			self.canvas.create_text(30, 35 + (n+1) * 70, text = str(n),
							 fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))
	 	#copy matrix to screen.
		self.displayUI()

	 	#Place score on screen
		(BLACK, WHITE) = self.state.score()
		stng = 'BLACK = ' + str(BLACK) + '\nWHITE  = ' + str(WHITE)
		self.score_id = self.canvas.create_text(750, 200, text = stng, fill = 'Yellow',  font = ('Helvetica', 20, 'bold'))

		stng = "Avaliable moves:" + '\n'
		legal_moves = self.state.get_possible_moves(1)
		counter=0
		for pos in legal_moves:
			if counter%4 == 0:
				stng = stng + '\n'
			stng = stng + str(chr(pos[1]+97)) + str(pos[0]) +" "
			counter=counter+1
		self.ava_id = self.canvas.create_text (755,350,text = stng, fill = 'white',  font = ('Helvetica', 20, 'bold'))

		#print previous move on miniture board
		position = "previous move: "+ "N/A"
		self.previous_id = self.canvas.create_text(750, 250, text = position, \
							 fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))
		self.messgae_id = ""
		self.gameoverID = ""

	def click_black(self,event):
		humanIsMove = False
		humanIsMove = self.humanMove(event, 1)
		computerIsMove = False
		if humanIsMove:
			computerIsMove = self.computerMove(-1)
		if computerIsMove:
			if self.state.gameover():
				self.endGameUI()
			return
	def click_white(self,event):
		humanIsMove = False
		humanIsMove = self.humanMove(event, -1)
		if self.state.gameover():
			self.endGameUI()
			return
		else:
			computerIsMove = False
			if humanIsMove:
				computerIsMove = self.computerMove(1)
			if computerIsMove:
				if self.state.gameover():
					self.endGameUI()
					return
	def self_play_black(self):
		book = Book()
		sQ = SQagent(book)
		record_list =[]
		self.canvas.delete(self.gameoverID)
		while (not self.state.gameover()):
			#print "here"
			sQ_legal_moves = self.state.get_possible_moves(1)
			if len(sQ_legal_moves)>0:
				next_move = sQ.predict(self.state, 1)
				record_list.append((self.state,next_move, 1))
				self.state = next_move
				self.displayUI()

			W_possible_moves = self.state.get_possible_moves(-1)
			if len(W_possible_moves)>0:
				pre_move, next_move = alpha_beta_search(self.state, 3, -1)
				#print self.state, next_move
				record_list.append((self.state,next_move, -1))
				self.state = next_move
				self.displayUI()
				self.canvas.delete(self.score_id)
				self.canvas.delete(self.previous_id)

			 	#update the score board
				(BLACK, WHITE) = self.state.score()
				stng = 'BLACK = ' + str(BLACK) + '\nWHITE  = ' + str(WHITE)
				self.score_id = self.canvas.create_text(750, 200, text = stng, \
									 fill = 'Yellow',  font = ('Helvetica', 20, 'bold'))

			 	#print previous move on miniture board
				position = "previous move: "+ str(chr(pre_move[0]+97)) + str(pre_move[1])
				self.previous_id = self.canvas.create_text(750, 250, text = position, \
									 fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))

				#update the avaliale moves board
				B_legal_moves = self.state.get_possible_moves(1)
				self.canvas.delete(self.ava_id)
				stng = "Avaliable moves:" + '\n'
				counter = 0
				for pos in B_legal_moves:
					if counter%4 == 0:
						stng = stng + '\n'
					stng = stng + str(chr(pos[1]+97)) + str(pos[0]) +" "
					counter = counter + 1
				self.ava_id = self.canvas.create_text (755,350,text = stng, fill = 'white',  font = ('Helvetica', 20, 'bold'))
			else:
				if len(W_possible_moves)==0:
					self.canvas.delete(self.messgae_id)
					text = "Computer has no valid moves this round"
					self.messgae_id = self.canvas.create_text(330, 700, text = text, \
										fill = 'RED', font = ('Helvetica', 20, 'bold'))

			if self.state.gameover():
				winner, loser = self.endGameUI()
				sQ.train(winner, loser, record_list)
		return

	def self_play_white(self):
		book = Book()
		sQ = SQagent(book)
		record_list =[]
		self.canvas.delete(self.gameoverID)
		while (not self.state.gameover()):
			print "here1"
			W_possible_moves = self.state.get_possible_moves(1)
			if len(W_possible_moves)>0:
				print "here2"
				pre_move, next_move = alpha_beta_search(self.state, 3, 1)
				print next_move.board
				#print self.state, next_move
				record_list.append((self.state,next_move, 1))
				self.state = next_move
				self.displayUI()
				self.canvas.delete(self.score_id)
				self.canvas.delete(self.previous_id)

			 	#update the score board
				(BLACK, WHITE) = self.state.score()
				stng = 'BLACK = ' + str(BLACK) + '\nWHITE  = ' + str(WHITE)
				self.score_id = self.canvas.create_text(750, 200, text = stng, \
									 fill = 'Yellow',  font = ('Helvetica', 20, 'bold'))

			 	#print previous move on miniture board
				position = "previous move: "+ str(chr(pre_move[0]+97)) + str(pre_move[1])
				self.previous_id = self.canvas.create_text(750, 250, text = position, \
									 fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))

				#update the avaliale moves board
				B_legal_moves = self.state.get_possible_moves(1)
				self.canvas.delete(self.ava_id)
				stng = "Avaliable moves:" + '\n'
				counter = 0
				for pos in B_legal_moves:
					if counter%4 == 0:
						stng = stng + '\n'
					stng = stng + str(chr(pos[1]+97)) + str(pos[0]) +" "
					counter = counter + 1
				self.ava_id = self.canvas.create_text (755,350,text = stng, fill = 'white',  font = ('Helvetica', 20, 'bold'))
			else:
				if len(W_possible_moves)==0:
					self.canvas.delete(self.messgae_id)
					text = "Computer has no valid moves this round"
					self.messgae_id = self.canvas.create_text(330, 700, text = text, \
										fill = 'RED', font = ('Helvetica', 20, 'bold'))

			sQ_legal_moves = self.state.get_possible_moves(-1)
			if len(sQ_legal_moves)>0:
				print "there"
				next_move = sQ.predict(self.state, -1)
				record_list.append((self.state,next_move, -1))
				self.state = next_move
				self.displayUI()
			else:
				print "huh?"
			if self.state.gameover():
				winner, loser = self.endGameUI()
				sQ.train(winner, loser, record_list)
		return

	def endGameUI(self):
		self.canvas.create_text(330, 350, text = "GAME OVER", \
							 fill = 'RED',  font = ('Helvetica', 40, 'bold'))
		self.canvas.delete(self.messgae_id)
		(BLACK, WHITE) = self.state.score()
		if BLACK>WHITE:
			winner = 1
			loser = -1
			result = "Your have won"
		elif WHITE > BLACK:
			winner = -1
			loser = 1
			result = "Computer has won"
		else:
			winner = 0
			loser = 0
			result = "Tie"
		self.messgae_id = self.canvas.create_text(330, 700, text = result, \
		fill = 'RED', font = ('Helvetica', 20, 'bold'))
		return winner, loser

	def loop(self, color, round):
		if color=="black":
			for i in range(0, int(round)):
				self.self_play_black()
				root = State()
				self.state = root
				self.canvas.delete("all")
				self.setUpInitialBoard()
				self.displayUI()
				print "round = " + str(i)
		else:
			for i in range(0, int(round)):
				self.self_play_white()
				root = State()
				self.state = root
				self.canvas.delete("all")
				self.setUpInitialBoard()
				self.displayUI()
				print "round = " + str(i)
		return

	def humanMove(self,event, color):
		c = (event.x-50)//70
		r = (event.y-70)//70
		pos_input = (r,c)
		legal_moves = self.state.get_possible_moves(color)

		#print "Length of legal moves:" + str(len(legal_moves))
		if len(legal_moves)>0:
			if pos_input in legal_moves:
				#print "yes"
				self.state.move_to(pos_input[0],pos_input[1],color)
				self.displayUI()
					#--erase old score and previous move
				self.canvas.delete(self.score_id)
				self.canvas.delete(self.previous_id)
				self.canvas.delete(self.messgae_id)

			 	#--print new score
				(BLACK, WHITE) = self.state.score()
				stng = 'BLACK = ' + str(BLACK) + '\nWHITE  = ' + str(WHITE)
				self.score_id = self.canvas.create_text(750, 200, text = stng, \
									 fill = 'Yellow',  font = ('Helvetica', 20, 'bold'))

			 	#--print previous move on miniture board
				position = "previous move: "+ str(chr(pos_input[0]+97)) + str(pos_input[1])
				self.previous_id = self.canvas.create_text(750, 250, text = position, \
									 fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))
				return True
			else:
				self.canvas.delete(self.messgae_id)
				text = "Your move is not valid"
				self.messgae_id = self.canvas.create_text(330, 700, text = text, \
									fill = 'RED', font = ('Helvetica', 20, 'bold'))
		else:
			self.canvas.delete(self.messgae_id)
			text = "Your have no valid moves this round"
			self.messgae_id = self.canvas.create_text(330, 700, text = text, \
			fill = 'RED', font = ('Helvetica', 20, 'bold'))
			return True

	def computerMove(self, color):
		W_possible_moves = self.state.get_possible_moves(color)
		if len(W_possible_moves)>0:
			pre_move, self.state = alpha_beta_search(self.state, 5, color)
			self.displayUI()
			self.canvas.delete(self.score_id)
			self.canvas.delete(self.previous_id)

		 	#update the score board
			(BLACK, WHITE) = self.state.score()
			stng = 'BLACK = ' + str(BLACK) + '\nWHITE  = ' + str(WHITE)
			self.score_id = self.canvas.create_text(750, 200, text = stng, \
								 fill = 'Yellow',  font = ('Helvetica', 20, 'bold'))

		 	#print previous move on miniture board
			position = "previous move: "+ str(chr(pre_move[0]+97)) + str(pre_move[1])
			self.previous_id = self.canvas.create_text(750, 250, text = position, \
								 fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))

			#update the avaliale moves board
			B_legal_moves = self.state.get_possible_moves(-color)
			self.canvas.delete(self.ava_id)
			stng = "Avaliable moves:" + '\n'
			counter = 0
			for pos in B_legal_moves:
				if counter%4 == 0:
					stng = stng + '\n'
				stng = stng + str(chr(pos[1]+97)) + str(pos[0]) +" "
				counter = counter + 1
			self.ava_id = self.canvas.create_text (755,350,text = stng, fill = 'white',  font = ('Helvetica', 20, 'bold'))
		else:
			if len(W_possible_moves)==0:
				self.canvas.delete(self.messgae_id)
				text = "Computer has no valid moves this round"
				self.messgae_id = self.canvas.create_text(330, 700, text = text, \
									fill = 'RED', font = ('Helvetica', 20, 'bold'))
		return True

