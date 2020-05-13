def song_decoder(song):

    song = song.replace("WUBWUBWUB", "WUB")
    song = song.replace("WUBWUB", "WUB")
    song = song.replace("WUB", " ")
    song = song.strip()
    
    return song

song = 'WUBAWUBBWUBCWUB'

res = song_decoder(song)
print(res)