def city_country(city_name, country):
    """return formatted city and country name"""
    formatted_string = f"{city_name.title()}, {country.title()}"
    return formatted_string

formatted_string = city_country('santiago', 'chile')
print(formatted_string)


def make_album(artist_name, album_title, no_of_songs=None):
    """Return album dictionary with information"""
    if no_of_songs:
        album = {'artist': artist_name, 'title': album_title, 'songs': no_of_songs}
    else:
        album = {'artist': artist_name, 'title': album_title}
    
    return album

album_0 = make_album('rabbi', 'think python', 23)
album_1 = make_album(artist_name='piash', album_title='python crash course')
album_2 = make_album(album_title='effective python', artist_name='borna')

print(album_0)
print(album_1)
print(album_2)


while True:
    print("\nPlease tell me artist name:")
    print("(enter 'q' at any time to quit)")

    artist_name = input('Artist name: ')
    if artist_name == 'q':
        break

    album_title = input('Album title: ')
    if album_title == 'q':
        break

    album = make_album(artist_name, album_title)
    print(album)