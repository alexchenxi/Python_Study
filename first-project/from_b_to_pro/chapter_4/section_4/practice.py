# 4.10
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"The first three items in the list are: ")
for num in list[:3]:
    print(f"{num}\t")
print(f"The middle three items in the list are: ")
for num in list[3:6]:
    print(f"{num}\t")
print(f"The last three items in the list are: ")
for num in list[-3:]:
    print(f"{num}\t")

games = ["GTA6", "Red Dead Dedemption II", "TX3"]
friend_games = games[:]
games.append("NBA2K")
friend_games.append("Rim World")
print("My games are: ")
for game in games:
    print(game)

print("Friend's games are: ")
for game in friend_games:
    print(game)
