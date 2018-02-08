def count_games(file_name):
	file = open(file_name,"r")
	game = file.readlines()
	return len(game)

def decide(file_name, year):
	if str(year) in open(file_name).read():
		return True
	else:
		return False

def get_latest(file_name):
	file = open(file_name,"r")
	game = file.readlines()
	table =[]
	for i in game:
		x = i.split("\t")
		table.append(x[2])
	table = max(table)
	table2=[]
	for i in game:
		x = i.split("\t")
		if x[2] == table:
			table2.append(x[0])
	return table2[0]

def count_by_genre(file_name, genre):
	file = open(file_name, "r")
	count = 0
	for i in file:
		if genre in i:
			count +=1
	return count

def get_line_number_by_title(file_name, title):
	file = open(file_name, "r")
	count = 0
	for i in file:
		count +=1
		try:
			if title in i:
				return count
			else:
				return ("ValueError")


def sort_abc(file_name):
	file = open(file_name,"r")
	game = file.readlines()
	table =[]
	for i in game:
		x = i.split("\t")
		table.append(x[0])

	n = len(table)
	i = 0
	while i < n:
		j = 0
		while j <= n - 2:
			if table[j] > table[j + 1]:
				temp = table[j+1]
				table[j+1] = table[j]
				table[j] = temp
				j += 1
			else:
				j += 1
		i += 1
	return table

def get_genres(file_name):
	file = open(file_name,"r")
	game = file.readlines()
	table =[]
	for i in game:
		x = i.split("\t")
		table.append(x[3])
	return sorted(list(set(table))) #set remove duplicate

def when_was_top_sold_fps(file_name):
	file = open(file_name,"r")
	game = file.readlines()
	table =[]
	for i in game:
		x = i.split("\t")
		if x[3] == "First-person shooter":
			table.append(float(x[1]))
	table = str(max(table))
	table2=[]
	for i in game:
		x = i.split("\t")
		if x[1] == table:
			table2.append(x[2])
	table2 = int(table2[0])
	return table2
