import winsound
import time

playback_time=2.1
print('playback_time :'+str(playback_time))


# Play wav file
print('Windows Exclamation')
winsound.PlaySound('c:/windows/media/Windows Exclamation.wav', winsound.SND_FILENAME)

# Play sound from control panel settings
print('SystemQuestion')
winsound.PlaySound('SystemQuestion', winsound.SND_ALIAS)

# Play wav file from memory
print('Chimes')
data=open('c:/windows/media/Chimes.wav',"rb").read()
winsound.PlaySound(data, winsound.SND_MEMORY)

# Start playing the first bit of wav file asynchronously
print('Windows Proximity Connection')
winsound.PlaySound('c:/windows/media/Windows Proximity Connection.wav',
winsound.SND_FILENAME|winsound.SND_ASYNC)

# Change the sleep timing(in sec) to increase the playback time
# But don't let it go on for too long
time.sleep(playback_time)
# Before stopping it
winsound.PlaySound(None, 0)


# C:\Windows\Media
# Copy above path for windows predefined audio files that you can use
