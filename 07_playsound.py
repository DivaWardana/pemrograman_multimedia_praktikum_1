#import required module
from playsound3 import playsound

#for playing sample.mp3 file
sound = playsound('sample.mp3')
print('playing sound using playsound')
if sound.is_alive():
    print("Sound is still playing!")

# and stop them whenever you like.
sound.stop()