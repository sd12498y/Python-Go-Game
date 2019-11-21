from state import State
import numpy as np
import random
class SQagent():
	def __init__(self, book):
		self.book = book
		self.alpha = 1.0

	def train(self, winner, loser, records):
		print "Total number of moves = " + str(len(records))
		for record in records:
			current = record[0]
			next1 = record[1]
			player = int(record[2])
			#print player
			#print winner == player
			#print int(winner) == player
			#print loser == player
			#print int(loser) == player
			if int(winner) == player:
				score = 7.0
			elif int(loser) == player:
				score = -7.0
			else:
				score = 0.0
			#print score
			result = self.book.checkExist(current, next1)
			#print result
			if result == None: #the (state, action) pairs returned by WHITE, which are not initialized through the predict function
				c = ""
				n = ""
				for i in current.board.flatten():
					c = c + str(i)
				for j in next1.board.flatten():
					n = n + str(j)
				#print self.alpha*score
				self.book.book[(c, n)] = self.alpha*score
			else:
				self.book.book[result] = (1.0-self.alpha) * self.book.book[result] + self.alpha * score
		self.book.save(winner)



	def predict(self, state, player):
		child_list = state.get_successors(player)
		#print child_list
		pool =[]
		current = ""
		for i in state.board.flatten():
			current = current + str(i)
		#print child_list
		for child in child_list:
			next1 =""
			for item in child[1].board.flatten():
				next1 = next1+str(item)

			result = self.book.checkExist(state, child[1])
			#print current, next1
			if result == None:
				alpha_init = 1
				self.book.book[(current,next1)] = 999999.0
				#print self.book.book[(current, next1)]
				#print (current, next1) in self.book.book
				temp = self.book.checkExist(state, child[1])
				#print temp
				#print (current, next1) == temp
				pool.append((999999.0, child[1]))
			else:
				pool.append((self.book.book[result], child[1]))
		#print pool
		random.shuffle(pool)
		max1 = max(pool)[1]
		return max1
