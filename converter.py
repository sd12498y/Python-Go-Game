import os.path
import sys
from state import State

filename = sys.argv[1]
file = open(filename, "r")
record_list = list()
game = State()
print game.board
for line in file:
	if int(line[0])==0:
		player=1
	else:
		player=-1
	col = int(line[2])
	row = int(line[4])
	game.move_to(row, col, player)
	print game.board
	record_list.append((player,row,col))
(Black, White) = game.score()
if Black > White:
	Black_label = 1
	White_label = 0
elif White > Black:
	Black_label = 0
	White_label = 1
else:
	Black_label = 0.5
	White_label = 0.5

print Black_label, White_label
file_name = os.path.splitext(filename)[0]
new_file_name = file_name+"_Sunday_format.txt"
new_file = open(new_file_name,"w")
for record in record_list:
	if record[0]==1:
		label = Black_label
	else:
		label = White_label
	string = str(record[0])+","+str(record[1])+","+str(record[2])+","+str(label) + "\n"
	new_file.write(string)



