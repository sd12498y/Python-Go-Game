def min_max_search(node, turn, max_depth):
	if turn == max_depth:
		return evaluate(node)
	else:
		if turn%2 == 0:
			function = max
			player = -1
		else:
			function = min
			player=1
		child_list = node.get_successors(player)
		poll = []
		for child in child_list:
			poll.append((min_max_search(child[1],turn+1, max_depth),child[1]))
		if turn==0 and len(poll)>0:
			return function(poll)[1]
		elif len(poll)>0:
			return function(poll)[0]

def alpha_beta_search(node, max_depth, player):
	tracker = 0
	v, new_board = max_value(node, 0, float("-inf"), float("inf"), max_depth, player)
	#print new_board
	return new_board[0],new_board[1]

def max_value(node, turn, alpha, beta, max_depth, player, **kwargs):
	tracker=kwargs.get('tracker')
	#print "Max" + str(tracker)
	#tracker = tracker+1
	#print "turn: " + str(turn)
	if turn == max_depth:
		#print "here"
		#print "Max_depth reached: " + str(evaluate(node))
		#print evaluate(node)
		return evaluate(node),((0,0),node)
	else:
		v = float("-inf")
		child_list = node.get_successors(player)
		#print child_list
		new_board=((0,0),node)
		#print child_list
		for child in child_list:
			if not tracker==None:
				#print "kk" + str(tracker)
				val, child_board = min_value(child[1],turn+1,alpha,beta, max_depth, player,tracker=tracker)
				v = max(v,val)
			else:
				val, child_board = min_value(child[1],turn+1,alpha,beta, max_depth, player)
				v = max(v,val)
			if v >= beta:
				#print "gg"
				return v, ((0,0),child[1])
			alpha = max(alpha,v)
			new_board = child
			#print child
			#print "alpha: " + str(alpha)
		#print new_board
		return v, new_board

def min_value(node, turn, alpha, beta, max_depth, player, **kwargs):
	tracker=kwargs.get('tracker')
	#print "Min" + str(tracker)
	#tracker = tracker+1
	#print "turn: " + str(turn)
	if turn == max_depth:
		#print "here"
		#print "Max_depth reached: " + str(evaluate(node))
		#print evaluate(node)
		return evaluate(node),((0,0),node)
	else:
		#print "here"
		v = float("inf")
		child_list = node.get_successors(-player)
		#print child_list
		new_board=((0,0),node)
		for child in child_list:
			if not tracker==None:
				val, child_board = max_value(child[1],turn+1,alpha,beta, max_depth,player, tracker=tracker)
				v = min(v, val)
			else:
				val, child_board = max_value(child[1],turn+1,alpha,beta,max_depth, player)
				v = min(v, val)
			if v <= alpha:
				#print "min prune"
				#print "alpha" + str(alpha)
				#print "there"
				return v, ((0,0),child[1])
			beta = min(beta,v)
			#print child
			new_board = child
			#print "beta: "+ str(beta)
		#print new_board
		return v, new_board

def evaluate(node):
	table=(99,-8,8,6,6,8,-8,99,-8,-24,-4,-3,-3,-4,-24,-8,8,-4,7,4,4,7,-4,8,6,-3,4,0,0,4,-3,6,6,-3,4,0,0,4,-3,6,8,-4,7,4,4,7,-4,8,-8,-24,-4,-3,-3,-4,-24,-8,99,-8,8,6,6,8,-8,99)
	W_sum=0
	B_sum=0
	counter=0
	for r in range(0,8):
		for c in range(0,8):
			if node.board[r][c] == -1:
				W_sum=W_sum+table[counter]
			elif node.board[r][c] == 1:
				B_sum=B_sum+table[counter]
			counter = counter+1
	return W_sum-B_sum