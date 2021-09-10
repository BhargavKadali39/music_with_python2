import winsound
import time

playback_time=2.1
print('playback_time :'+str(playback_time))

# Play wav file
print('\nWindows Exclamation\n')
winsound.PlaySound('c:/windows/media/Windows Exclamation.wav', winsound.SND_FILENAME)

# Play sound from control panel settings
print('SystemQuestion\n')
winsound.PlaySound('SystemQuestion', winsound.SND_ALIAS)

# Play wav file from memory
print('Chimes\n')
data=open('c:/windows/media/Chimes.wav',"rb").read()
winsound.PlaySound(data, winsound.SND_MEMORY)

# Start playing the first bit of wav file asynchronously
print('Windows Proximity Connection\n')
winsound.PlaySound('c:/windows/media/Windows Proximity Connection.wav',
winsound.SND_FILENAME|winsound.SND_ASYNC)

# Change the sleep timing(in sec) to increase the playback time
# But don't let it go on for too long
time.sleep(playback_time)
# Before stopping it
winsound.PlaySound(None, 0)

print('Thank you')

# C:\Windows\Media
# Copy above path for windows predefined audio files that you can use
