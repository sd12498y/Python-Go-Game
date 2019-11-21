class Record:
	dics = []
	mobility = []
	player_stability_gained = []
	oppo_stability_gained = []
	legal_moves = []
	ones = []
	zeros = []
	player=[]

	def __init__ (self, dics, mobility, player_stability_gained, oppo_stability_gained, legal_moves, player):
		self.ones = np.array([ [1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],])
		self.zeros = np.array([[0, 0, 0, 0, 0, 0, 0, 0,],
			[0, 0, 0, 0, 0, 0, 0, 0,],
			[0, 0, 0, 0, 0, 0, 0, 0,],
			[0, 0, 0, 0, 0, 0, 0, 0,],
			[0, 0, 0, 0, 0, 0, 0, 0,],
			[0, 0, 0, 0, 0, 0, 0, 0,],
			[0, 0, 0, 0, 0, 0, 0, 0,],
			[0, 0, 0, 0, 0, 0, 0, 0,],])
		self.dics = dics #3 planes
		self.mobility = mobility #8planes
		self.player_stability_gained = player_stability_gained #8 planes
		self.oppo_stability_gained = oppo_stability_gained #8 planes
		self.legal_moves = legal_moves #1plane
		self.player = player

import chess
import chess.polyglot
board = chess.Board()
print boa








