def get_most_played(file_name):
    file = open(file_name,"r")
    game = file.readlines()
    tom =[]
    for i in game:
        z = i.split("\t")
        tom.append(float(z[1]))
    tom = str(round(max(tom)))
    tom2=[]
    for i in game:
        x = i.split("\t")
        if x[1] == tom:
            tom2.append(x[0])
    return tom2[0]

def sum_sold(file_name):
    file = open(file_name,"r")
    game = file.readlines()
    tom =[]
    for i in game:
        z = i.split("\t")
        tom.append(float(z[1]))
    s = sum(tom)
    return s

def get_selling_avg(file_name):
    file = open(file_name,"r")
    game = file.readlines()
    tom =[]
    for i in game:
        z = i.split("\t")
        tom.append(float(z[1]))
    s = sum(tom)
    return s/(len(tom)) #round

def count_longest_title(file_name):
    file = open(file_name,"r")
    game = file.readlines()
    tom =[]
    for i in game:
        z = i.split("\t")
        tom.append(z[0])
    return len(max(tom, key=len))

def get_date_avg(file_name):
    file = open(file_name,"r")
    game = file.readlines()
    tom =[]
    for i in game:
        z = i.split("\t")
        tom.append(float(z[2]))
    s = sum(tom)
    return round(s/(len(tom)))

def get_game(file_name, title):
    file = open(file_name,"r")
    game = file.readlines()
    tom =[]
    for i in game:
        z = i.split("\t")
        if z[0] == title:
            break
    final=[]
    for item in z:
        final.append(item.strip())
    final.pop(1)
    final.pop(1)
    final.insert(1,float(z[1]))
    final.insert(2,float(z[2]))
    return final
