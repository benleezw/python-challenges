from random import randint

DominicFike = [
    "Frisky - Dominic Fike",
    "3 Nights - Dominic Fike",
    "Where's The Weed At? - Dominic Fike",
    "Mona Lisa - Dominic Fike",
    "Babydoll - Dominic Fike",
    "Mama's Boy - Dominic Fike",
    "Why - Dominic Fike",
    "Chicken Tenders - Dominic Fike",
    "Vampire - Dominic Fike",
    "Whats For Dinner? - Dominic Fike"
]

jid = [
    "Galaxy - JID",
    "Sistanem - JID",
    "Enemies - JID",
    "Jerma - JID",
    "Stars - JID",
    "Crack Sandwich - JID",
    "151 Rum - JID",
    "Surround Sound - JID",
    "Dance Now - JID",
    "Can't Punk Me - JID"
]

Joji = [
    "Glimpse of Us - Joji",
    "Joji - Joji",
    "Die For You - Joji",
    "Sanctuary - Joji",
    "SLOW DANCING IN THE - Joji",
    "ATTENTION - Joji",
    "WANTED U - Joji",
    "TEST DRIVE - Joji",
    "Ew - Joji",
    "MODUS - Joji"
]

c418 = [
    "Key - C418",
    "Door - C418",
    "Aria Math - C418",
    "Death - C418",
    "Subwoofer Lullaby - C418",
    "Living Mice - C418",
    "Dry Hands - C418",
    "Wet Hands - C418",
    "Minecraft - C418",
    "Sweden - C418"
]

Laufey = [
    "From the Start - Laufey",
    "Dreamer - Laufey",
    "Second Best - Laufey",
    "Valentine - Laufey",
    "Falling Behind - Laufey",
    "Let You Break My Heart Again - Laufey",
    "Promise - Laufey",
    "Haunted - Laufey",
    "Lovesick - Laufey",
    "Misty - Laufey"
]

Radiohead = [
    "15 Step - Radiohead",
    "Bodysnatchers - Radiohead",
    "Nude - Radiohead",
    "Weird Fishes/ Arpeggi - Radiohead",
    "All I Need - Radiohead",
    "Faust Arp - Radiohead",
    "Reckoner - Radiohead",
    "House Of Cards - Radiohead",
    "Jigsaw Falling Into Place - Radiohead",
    "Videotape - Radiohead",
]

beabadoobee = [
    "Care - beabadoobee",
    "Worth It - beabadoobee",
    "Dye It Red - beabadoobee",
    "Back To Mars - beabadoobee",
    "Charlie Brown - beabadoobee",
    "Emo Song - beabadoobee",
    "Sorry - beabadoobee",
    "Sorry - beabadoobee",
    "Further Away - beabadoobee",
    "Horen Sarrison - beabadoobee",
    "How Was Your Day?"
]

Hozier = [
    "Take Me To Church - Hozier",
    "Cherry Wine - Hozier",
    "De Shelby (Part 1) - Hozier",
    "Eat Your Young - Hozier",
    "Like Real People Do - Hozier",
    "Shrike - Hozier",
    "Almost (Sweet Music) - Hozier",
    "De Shelby (Part 2) - Hozier",
    "Would That I - Hozier",
    "Francesca - Hozier"
]

SleepingAtLast = [
    "Sun - Sleeping At Last",
    "Venus - Sleeping At Last",
    "Mercury - Sleeping At Last",
    "Earth - Sleeping At Last",
    "Moon - Sleeping At Last",
    "Jupiter - Sleeping At Last",
    "Mars - Sleeping At Last",
    "Saturn - Sleeping At Last",
    "Pluto - Sleeping At Last",
    "Venus - Sleeping At Last"
]

TheWombats = [
    "Greek Tragedy - The Wombats",
    "Let's Dance to Joy Division - The Wombats",
    "Kill the Director - The Wombats",
    "Turn - The Wombats",
    "Moving to New York - The Wombats",
    "Pink Lemonade - The Wombats",
    "Tokyo (Vampires & Wolves) - The Wombats",
    "Lemon to a Knife Fight - The Wombats",
    "Backfire at the Disco - The Wombats",
    "Lost in the Post - The Wombats"
]

artistlist = [DominicFike, jid, Joji, c418, Laufey]
artistorder = []
artistorder_pos = 0
playlist = []
songcount = 0
while songcount < 10:
    currentartist = randint(0,len(artistlist) - 1)
    currentsong = randint(0,9)
    if len(playlist) > 1:
        # print(currentartist)
        # print(artistorder[artistorder_pos - 2])
        # print(artistorder[artistorder_pos - 3])
        # print()
        while currentartist  == artistorder[artistorder_pos - 1] or currentartist  == artistorder[artistorder_pos - 2] or currentartist == artistorder[artistorder_pos - 3]:
            # print("reshuffling")
            currentartist = randint(0,len(artistlist) - 1)
            currentsong = randint(0,9)
    # print(currentartist)
    # print(artistlist[currentartist][currentsong])
    while str(artistlist[currentartist][currentsong]) in playlist:
        currentsong = randint(0,9)
    playlist.append(artistlist[currentartist][currentsong])
    artistorder.append(currentartist)
    # print(artistorder)
    songcount += 1
    artistorder_pos += 1
print(playlist)
    

# print(artistlist[1][2])
# print()

