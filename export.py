import reports

put1 = input("Game title: ")
put2 = input("Year: ")
put3 = input("Genre: ")

f = open("/home/tomek/Documents/pbwp-3rd-si-game-statistics/export.txt", "w+")
f.write(str(reports.count_games("game_stat.txt"))+'\n')
f.write(str(reports.decide("game_stat.txt", put2))+'\n')
f.write(str(reports.get_latest("game_stat.txt"))+'\n')
f.write(str(reports.count_by_genre("game_stat.txt", put3))+'\n')
f.write(str(reports.get_line_number_by_title("game_stat.txt", put1))+'\n')
f.write(str(reports.sort_abc("game_stat.txt"))+'\n')
f.write(str(reports.get_genres("game_stat.txt"))+'\n')
f.write(str(when_was_top_sold_fps("game_stat.txt"))+'\n')
f.close()
