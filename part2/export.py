import reports

put1 = input("Game title: ")
put2 = input("Genre: ")

f = open("/home/tomek/Documents/pbwp-3rd-si-game-statistics/part2/export.txt", "w+")
f.write(str(reports.get_most_played("game_stat.txt"))+'\n')
f.write(str(reports.sum_sold("game_stat.txt"))+'\n')
f.write(str(reports.get_selling_avg("game_stat.txt"))+'\n')
f.write(str(reports.count_longest_title("game_stat.txt"))+'\n')
f.write(str(reports.get_date_avg("game_stat.txt"))+'\n')
f.write(str(reports.get_game("game_stat.txt", put1))+'\n')
f.close()
