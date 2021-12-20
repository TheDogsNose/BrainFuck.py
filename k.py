song = ['always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life']
song_iter = iter(song)
for sing in song_iter:
    print (sing)
    if sing == 'look':
        next(song_iter)
        next(song_iter)
        next(song_iter)
        print ('a' + next(song_iter))