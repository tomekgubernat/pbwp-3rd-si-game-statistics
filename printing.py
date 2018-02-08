import reports

put1 = input("Game title: ")
put2 = input("Year: ")
put3 = input("Genre: ")

print("\n")

print(reports.count_games("game_stat.txt"))
print(reports.decide("game_stat.txt", put2))
print(reports.get_latest("game_stat.txt"))
print(reports.count_by_genre("game_stat.txt", put3))
print(reports.get_line_number_by_title("game_stat.txt", put1))
print(reports.sort_abc("game_stat.txt"))
print(reports.get_genres("game_stat.txt"))
print(reports.when_was_top_sold_fps("game_stat.txt"))
