import json
import random


# Load tracks
with open('books.json', 'r') as stream:
    tracks = json.load(stream)
track_list = [track for track in tracks]

# Track numbers
track_numbers = {}
count = 1
for track in tracks:
    track_numbers[track] = count
    count += 1

# Travel history
seen = {}
for track in tracks:
    seen[track] = []

# Generator
tracks_completed = []
reading_list = []
while tracks_completed.__len__() < track_list.__len__():
    for track in tracks:
        track_number = track_numbers[track]
        books = tracks[track]

        while True:
            book = random.choice(books)
            if book not in seen[track]:
                reading = (track_number, book)

                reading_list.append(reading)
                seen[track].append(book)

                if seen[track].__len__() == books.__len__():
                    if track not in tracks_completed:
                        tracks_completed.append(track)
                    seen[track] = []
                break

# Output for Color Note.
# Print
for reading in reading_list:
    track_number, book = reading
    print(book)

# File
with open('out/plan-colornote.txt', 'w+') as stream:
    for reading in reading_list:
        track_number, book = reading
        stream.write('[ ] {}. {}\n'.format(track_number, book))
