#Loads gtts, which handles text to speech via google text to speech api
#pygame is responsible for the mp3 playing
from gtts import gTTS
from pygame import mixer
import os
def Input():
    #Asks user for the string to be read
    x = input("What would you like to be read?")
    #Creates mp3 file of the string being read
    c = "1" + ".mp3"
    tts = gTTS(text=x, lang="en")
    tts.save(c)
    #Initializes audio to be played, loads the mp3, and then plays the mp3
    mixer.init()
    mixer.music.load(c)
    mixer.music.play()
    input("Press enter to exit the program")
    return (c)
    

def Parse():
    #Opens the file to be parsed and saves the data as variable (f)
    k = input("What would you like to read? (Note that it must be in a .txt format)")
    f = open(k, 'r')
    #Reads the contents and stores it as variable (c)
    o = f.read()
    #Stores the contents of the file as an mp3
    c = "1" + ".mp3"
    tts = gTTS(text=o, lang="en")
    tts.save(c)
    #Initializes audio to be played, loads the mp3, and then plays the mp3
    mixer.init()
    mixer.music.load(c)
    mixer.music.play()
    input("Press enter to exit the program")
    return (c)

p = input("Would you like to Input or Parse?")
if p == "Parse":
    h = Parse()
    mixer.quit()
    os.remove(h)

elif p == "Input":
    h = Input()
    mixer.quit()
    os.remove(h)

else:
    quit
