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

artistlist = [jid, DominicFike, Joji, c418, Laufey]
playlist = []
songcount = 0
prevartist = 0
while songcount < 10:
    currentartist = randint(0,len(artistlist) - 1)
    currentsong = randint(0,9)
    while currentartist == prevartist:
        currentartist = randint(0,len(artistlist) - 1)
    if len(playlist) > 2:
        # print(playlist[songcount - 3])
        while playlist[songcount - 3] in artistlist[currentartist]:
            currentartist = randint(0,len(artistlist) - 1)
    # print(currentartist)
    # print(artistlist[currentartist][currentsong])
    while str(artistlist[currentartist][currentsong]) in playlist:
        currentsong = randint(0,9)
    playlist.append(artistlist[currentartist][currentsong])
    prevartist = currentartist
    songcount += 1

print(playlist)
    

# print(artistlist[1][2])
# print()

