#User Albums

def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs is not None:
        album["songs"] = songs
    return album

while True:
    artist = input("Nama artis (ketik q untuk berhenti): ")
    if artist.lower() == "q":
        break
    title = input("Judul album: ")
    print(make_album(artist, title))
