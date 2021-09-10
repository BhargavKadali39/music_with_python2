import winsound
import time

# Play wav file
winsound.PlaySound('c:/windows/media/Windows Exclamation.wav', winsound.SND_FILENAME)

# Play sound from control panel settings
winsound.PlaySound('SystemQuestion', winsound.SND_ALIAS)

# Play wav file from memory
data=open('c:/windows/media/Chimes.wav',"rb").read()
winsound.PlaySound(data, winsound.SND_MEMORY)

# Start playing the first bit of wav file asynchronously
winsound.PlaySound('c:/windows/media/Windows Proximity Connection.wav',
winsound.SND_FILENAME|winsound.SND_ASYNC)

# Change the sleep timing(in sec) to increase the playback time
# But don't let it go on for too long
time.sleep(2.1)
# Before stopping it
winsound.PlaySound(None, 0)


# C:\Windows\Media
# Copy above path for windows predefined audio files that you can use
