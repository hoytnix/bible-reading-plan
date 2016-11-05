Bible Reading Plan
==================

Generate a plan for reading the Bible, in an unconventional order.


## What it does

The software divides the Bible into nine-different sections ("tracks"):
+ Mosaic
+ Old Testament Narrative
+ Wisdom
+ Major Prophets
+ Minor Prophets
+ Gospel
+ Pauline Epistles
+ General Epistles
+ Revelation


_1_. Each iteration a book from each track is randomly chosen; it will not be chosen again until each book has been chosen once.

The "Revelation"-track has one book, so it will always be chosen.
The "Gospel"-track has five books, so none will repeat until all have been chosen.


_2_. The cycle continues until every book of the Bible has been chosen at least once. Shorter tracks, especially Revelation, will occur much more frequently, while a book in a longer track should only occur once.

This is intentional: tracks such as the Gospel, Revelation, Wisdom, and the Major Prophets can be considered more important than OT Narrative books such as Ezra. :)


_3_. Import the list into a supported service and soak in the knowledge and glory of God.


## Usage

Generate a random plan with `python plan.py`.

Currently only [Colornote](https://www.colornote.com/) is supported. Upload the file `out/plan-colornote.txt` to [Google Drive](https://drive.google.com/drive/#), open with Colornote, and save the list. I recommend placing a widget to the note on your home-screen for easy access.

Each track has a number from _1_ - _9_. Start with the book from track _1_ and every day continue to the next track, finally going back to track _1_ after track _9_. Once you finish a book from a track, remove it from your list, and begin to read the first book with the same track number.

This design is intended for the reader to maintain view-points from each section of God's Word: because a track is touched _about once a week_, the material from one viewpoint should be fresh when similar material is mentioned in a book from a different section.

Purposefully, the book of Revelation is read _every nine-days_ or about _once a week_. This is because of the prophecy in Revelation 1:3:

> Blessed is he who reads and those who hear the words of the prophecy, and heed the things which are written in it; for the time is near." (Revelation 1:3 [NASB])

Additionally, the books of the Mosaic Law as well as the Gospel are rotated with the second-most frequency, besides Revelation, which is useful because these are two significant dispensations of time.


## Why did you...

### Place "Hebrews" in "General Epistles"?

Although Hebrews is widely believed to be written by Paul (myself included), the author himself decided to remain anonymous, which I believe is a good enough reason.


### Create this?

The Lord impressed upon me the design for this reading schedule, and I couldn't find any software which supported the functionality required to utilize it. So, I went old school with a checklist. :)
