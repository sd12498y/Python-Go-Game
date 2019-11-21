import numpy as np
from copy import deepcopy
from search import min_max_search, alpha_beta_search
class State():
	board = ""

	def __init__(self):
		self.createMatrix()

	def createMatrix(self): # = the initial position, with Black = 1, and white = -1.
		self.board = np.array([ [0, 0, 0, 0, 0, 0, 0, 0,],
				[0, 0, 0, 0, 0, 0, 0, 0,],
				[0, 0, 0, 0, 0, 0, 0, 0,],
				[0, 0, 0, -1, 1, 0, 0, 0,],
				[0, 0, 0, 1, -1, 0, 0, 0,],
				[0, 0, 0, 0, 0, 0, 0, 0,],
				[0, 0, 0, 0, 0, 0, 0, 0,],
				[0, 0, 0, 0, 0, 0, 0, 0,],])

	def get_successors(self,player):
		child_list = list()
		possible_list = self.get_possible_moves(player)
		if len(possible_list)>0:
			for pos in possible_list:
				child = State()
				child.board = deepcopy(self.board)
				row = pos[0]
				col = pos[1]
				child.move_to(row,col,player)
				child_list.append(((row,col),child))
		return child_list
	def get_possible_moves(self, player):
		if player == -1:
			actor = -1
			opponent=1
		else:
			actor = 1
			opponent=-1
		possible_list = set()
		for r in range(0,8):
			for c in range(0,8):
				#print i
				if self.board[r][c] == actor:
					#print self.board[r][c]
					# check left
					j_c=c-1
					count = 0
					while j_c>-1:
						#print j
						if self.board[r][j_c]==opponent:
							count = count + 1
							j_c = j_c - 1
							continue
						else:
							if count==0 or self.board[r][j_c]==actor:
								break
							else:
								possible_list.add((r,j_c))
								break
					# check top left
					j_r=r-1
					j_c=c-1
					count = 0
					while j_r > -1 and j_c > -1:
						#print j
						if self.board[j_r][j_c]==opponent:
							count = count + 1
							j_r = j_r-1
							j_c = j_c-1
							continue
						else:
							if count==0 or self.board[j_r][j_c]==actor:
								break
							else:
								possible_list.add((j_r,j_c))
								#child.display()
								break
					# check top
					j_r=r-1
					count = 0
					while j_r > -1:
						#print j
						#print "iam" + str(self.board[j_r][c])
						if self.board[j_r][c]==opponent:
							count = count + 1
							j_r = j_r - 1
							continue
						else:
							if count==0 or self.board[j_r][c]==actor:
								#print "checking top" + str(count)
								break
							else:
								#print "checking top..." + str(count)
								possible_list.add((j_r,c))
								break
					# check top right
					j_r=r-1
					j_c=c+1
					count = 0
					while j_r >-1 and j_c<8:
						#print j
						if self.board[j_r][j_c]==opponent:
							count = count + 1
							j_r = j_r - 1
							j_c = j_c + 1
							continue
						else:
							if count==0 or self.board[j_r][j_c]==actor:
								break
							else:
								possible_list.add((j_r,j_c))
								break
					# check right
					j_c=c+1
					count = 0
					while j_c<8:
						#print j
						if self.board[r][j_c]==opponent:
							count = count + 1
							j_c = j_c + 1
							continue
						else:
							if count==0 or self.board[r][j_c]==actor:
								break
							else:
								possible_list.add((r,j_c))
								break
					# check bottom right
					j_r=r+1
					j_c=c+1
					count = 0
					while j_r<8 and j_c<8:
						#print j
						if self.board[j_r][j_c]==opponent:
							count = count + 1
							j_r = j_r + 1
							j_c = j_c + 1
							continue
						else:
							if count==0 or self.board[j_r][j_c]==actor:
								break
							else:
								possible_list.add((j_r,j_c))
								break
					# check bottom
					j_r = r + 1
					count = 0
					while j_r<8:
						#print j
						if self.board[j_r][c]==opponent:
							count = count + 1
							j_r = j_r + 1
							continue
						else:
							if count==0 or self.board[j_r][c]==actor:
								break
							else:
								possible_list.add((j_r,c))
								break
					# check bottom left 
					j_r = r + 1
					j_c = c - 1
					count = 0
					while j_r<8 and j_c>-1:
						#print j
						if self.board[j_r][j_c]==opponent:
							count = count + 1
							j_r = j_r + 1
							j_c = j_c - 1
							continue
						else:
							if count==0 or self.board[j_r][j_c]==actor:
								break
							else:
								possible_list.add((j_r,j_c))
								break
		return possible_list

	def score(self): # returns the number of black disks and white disks.
		whiteTotal = 0; blackTotal = 0
		for r in range(8):
			for c in range (8):
				if self.board[r][c] ==  1: blackTotal += 1
				if self.board[r][c] == -1: whiteTotal += 1
		return (blackTotal, whiteTotal)

	def move_to(self, row, col, player): 	#player: black = 1, white = -1
		#print "moving..."+str(row)+str(col)
		if player == -1:
			actor = -1
			opponent=1
		else:
			actor = 1
			opponent=-1
		self.board[row][col]=actor
		r = row
		c = col
		# check left
		j_c=c-1
		count = 0
		while j_c > -1:
			#print j
			if self.board[r][j_c]==opponent:
				count = count + 1
				j_c = j_c - 1
				continue
			else:
				if count==0:
					break
				elif self.board[r][j_c]==actor:
					for k in range(j_c,c):
						self.board[r][k] = actor
					#child.display()
					break
				else:
					break
		# check top left
		j_r = r - 1
		j_c = c -1
		count = 0
		while j_r > -1 and j_c > -1:
			#print j
			if self.board[j_r][j_c]==opponent:
				count = count + 1
				j_r = j_r - 1
				j_c = j_c - 1
				continue
			else:
				if count==0:
					break
				elif self.board[j_r][j_c]==actor:
					for k in range(j_c,c):
						self.board[j_r][k] = actor
						j_r = j_r + 1
					#child.display()
					break
				else:
					break
		# check top
		j_r=r-1
		count = 0
		while j_r >-1:
			#print j
			if self.board[j_r][c]==opponent:
				count = count + 1
				j_r = j_r - 1
				continue
			else:
				if count==0:
					break
				elif self.board[j_r][c]==actor:
					for k in range(j_r,r):
						self.board[k][c] = actor
					break
				else:
					break
		# check top right
		j_r = r - 1
		j_c = c + 1
		count = 0
		while j_c < 8 and j_r > -1:
			#print j
			if self.board[j_r][j_c]==opponent:
				count = count + 1
				j_r = j_r - 1
				j_c = j_c + 1
				continue
			else:
				if count==0:
					break
				elif self.board[j_r][j_c]==actor:
					for k in range(j_r,r):
						self.board[k][j_c] = actor
						j_c = j_c - 1
					break
				else:
					break
		# check right
		j_c=c+1
		count = 0
		while j_c <8:
			#print j
			if self.board[r][j_c]==opponent:
				count = count + 1
				j_c = j_c + 1
				continue
			else:
				if count==0:
					break
				elif self.board[r][j_c]==actor:
					for k in range(c,j_c):
						self.board[r][k] = actor
					break
				else:
					break
		# check bottom right
		j_r = r + 1
		j_c = c + 1
		count = 0
		while j_r < 8 and j_c < 8:
			#print j
			if self.board[j_r][j_c]==opponent:
				count = count + 1
				j_r = j_r + 1
				j_c = j_c + 1
				continue
			else:
				if count==0:
					break
				elif self.board[j_r][j_c]==actor:
					for k in range(r,j_r):
						j_r = j_r - 1
						j_c = j_c - 1
						self.board[j_r][j_c] = actor
					break
				else:
					break
		# check bottom
		j_r=r+1
		count = 0
		while j_r<8:
			#print j
			if self.board[j_r][c]==opponent:
				count = count + 1
				j_r = j_r + 1
				continue
			else:
				if count==0:
					break
				elif self.board[j_r][c]==actor:
					for k in range(r,j_r):
						self.board[k][c] = actor
					break
				else:
					break
		# check bottom left 
		j_r = r+1
		j_c = c-1
		count = 0
		while j_r < 8 and j_c > -1:
			#print j
			if self.board[j_r][j_c]==opponent:
				count = count + 1
				j_r = j_r + 1
				j_c = j_c - 1
				continue
			else:
				if count==0:
					break
				elif self.board[j_r][j_c]==actor:
					for k in range(r,j_r):
						self.board[j_r][j_c] = actor
						j_r = j_r - 1
						j_c = j_c + 1
					break
				else:
					break

	def gameover(self):
		B_possible_moves = self.get_possible_moves(1)
		#print B_possible_moves
		W_possible_moces = self.get_possible_moves(-1)
		#print W_possible_moces
		#print len(B_possible_moves) + len(W_possible_moces)
		if len(B_possible_moves) + len(W_possible_moces) == 0:
			return True
		else:
			return False
	def getSymmetry(self):
		sy_list = []
		ro90 = np.rot90(self.board)
		ro180 = np.rot90(ro90)
		ro270 = np.rot90(ro180)
		s1 =""
		s2 =""
		s3=""
		s4=""
		for item in self.board.flatten():
			s1 = s1 + str(item)
		sy_list.append(s1)
		for item1 in ro90.flatten():
			s2 = s2 + str(item1)
		sy_list.append(s2)
		for item2 in ro180.flatten():
			s3 = s3 + str(item2)
		sy_list.append(s3)
		for item3 in ro270.flatten():
			s4 = s4 + str(item3)
		sy_list.append(s4)
		return sy_list
	def getInvertSymmetry(self):
		sy_list = []
		invt_board = np.flip(self.board,0)
		ro90 = np.rot90(invt_board)
		ro180 = np.rot90(ro90)
		ro270 = np.rot90(ro180)
		s1 =""
		s2 =""
		s3=""
		s4=""
		for item in invt_board.flatten():
			s1 = s1 + str(item)
		sy_list.append(s1)
		for item1 in ro90.flatten():
			s2 = s2 + str(item1)
		sy_list.append(s2)
		for item2 in ro180.flatten():
			s3 = s3 + str(item2)
		sy_list.append(s3)
		for item3 in ro270.flatten():
			s4 = s4 + str(item3)
		sy_list.append(s4)
		return sy_list
	def getCornerDiff(self, player):
		if player==1:
			actor=1
			opponent=-1
		else:
			actor=-1
			opponent=1
		actor_sum = 0
		opponent_sum = 0
		if self.board[0][0]==actor:
			actor_sum = opponent_sum + 1
		elif self.board[0][0]==opponent:
			opponent_sum = opponent_sum + 1
		if self.board[0][7]==actor:
			actor_sum = opponent_sum + 1
		elif self.board[0][7]==opponent:
			opponent_sum = opponent_sum + 1
		if self.board[7][0]==actor:
			actor_sum = opponent_sum + 1
		elif self.board[7][0]==opponent:
			opponent_sum = opponent_sum + 1
		if self.board[7][7]==actor:
			actor_sum = opponent_sum + 1
		elif self.board[7][7]==opponent:
			opponent_sum = opponent_sum + 1
		return actor_sum-opponent_sum

	def getMobility(self, player):
		if player==1:
			actor=1
			opponent=-1
		else:
			actor=-1
			opponent=1
			actor_sum = self.get_possible_moves(actor)
			opponent_sum = self.get_possible_moves(opponent)
		if actor_sum > opponent_sum:
			return 100.0*actor_sum/(actor_sum+opponent_sum)
		elif actor_sum < opponent_sum:
			return -(100.0*opponent_sum)/(actor_sum+opponent_sum);
		else: return 0



