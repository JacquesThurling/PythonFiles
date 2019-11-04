imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Waltz")
)

# My solution
for i in imelda:
    if i == imelda[3]:
        print("=" *6)

        for j in imelda[3]:
            print("\t", j)
    else:
        print(i)

# Other solution -  from course plus extras
print("=" * 10)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print("=" * 10)
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))

# When the tuple stores the items as a list
imelda = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Waltz")]
)

print(imelda)
imelda[3].append((5, "All for you"))

title, artist, year, tracks = imelda
tracks.append((6, "Eternity"))
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))

