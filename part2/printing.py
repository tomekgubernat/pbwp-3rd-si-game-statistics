import reports

put1 = input("Game title: ")
put2 = input("Genre: ")

print("\n")

print(reports.get_most_played("game_stat.txt"))
print(reports.sum_sold("game_stat.txt"))
print(reports.get_selling_avg("game_stat.txt"))
print(reports.count_longest_title("game_stat.txt"))
print(reports.get_date_avg("game_stat.txt"))
print(reports.get_game("game_stat.txt", put1))
