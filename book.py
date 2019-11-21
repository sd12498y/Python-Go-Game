import os.path
class Book():
	def __init__(self):
		self.book = dict()
		if os.path.exists("book.txt"):
			file = open("book.txt", "r")
			print "loading book..."
			for line in file:
				item = line.split(',')
				#convert the score to integer value
				self.book[(item[0],item[1])]=float(item[2])
			print "successfully loaded Book"

	def checkExist(self,current,next):
		sy_list1 = current.getSymmetry()
		insy_list1 = current.getInvertSymmetry()
		current_list = sy_list1+insy_list1
		sy_list2 = next.getSymmetry()
		insy_list2 = next.getInvertSymmetry()
		next_list = sy_list2+insy_list2

		for i in current_list:
			for j in next_list:
				if (i,j) in self.book:
					return (i,j)

		return None
		
	def save(self, *winner):
		file = open("book.txt","w")
		print "saving book..."
		counter = 0
		counter2 = 0
		for key in self.book:
			string = key[0]+","+key[1]+","+str(self.book[key])+',\n'
			if self.book[key] == 999999.0:
				counter = counter + 1
			else:
				counter2 = counter2 + 1
			file.write(string)
		print "finished"
		print "Total 99999.0 = " + str(counter)
		print "Total real value = " + str(counter2)
		file1 = open("learning_record.txt","a")
		string = str(counter) + "," + str(counter2) + ","
		#1=win, 0=lose, 0.5=tie
		if int(winner[0]) == 1:
			string = string + str(1) + ",\n"
		elif int(winner[0]) == -1:
			string = string + str(0) +",\n"
		else:
			string = string + str(0.5) +",\n"
		file1.write(string)
		file1.close()
		file.close()