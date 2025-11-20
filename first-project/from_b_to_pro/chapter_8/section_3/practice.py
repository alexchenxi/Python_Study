# 8.6
def city_country(city_name, country):
    return f'"{city_name.title()}, {country.title()}"'


print(city_country("suzhou", "china"))
print(city_country("Fairfax", "united states"))
print(city_country("London", "united kindom"))

print("###########################################")


# 8.7
def make_album(singer_name, album_name, songs_number=None):
    if songs_number:
        album = {
            "singer_name": singer_name,
            "album_name": album_name,
            "songs_number": songs_number,
        }
    else:
        album = {
            "singer_name": singer_name,
            "album_name": album_name,
        }
    return album


# print(make_album("David", "AEIOU", songs_number=1))
# print(make_album("Jay Chou", "Fantasy"))

print("###########################################")
# 8.8
while True:
    print("\nPlease input album's information:")
    print("(enter 'q' at any time to quit.)")
    singer_name_input = input("Singer name:")
    if singer_name_input == "q":
        break
    album_name_input = input("Album name:")
    if album_name_input == "q":
        break
    songs_number_input = input("Songs number:")
    if songs_number_input == "q":
        break

    print(make_album(singer_name_input, album_name_input, songs_number_input))
