from gtts import gTTS
import vlc
myobj = gTTS(text = 'My name is Hassan Bahnasy I LOVE ZAMALEK ',lang ='en',slow = False)
#saving the Converted audio in a mp3 file named
myobj.save("Test.mp3")
#Playing the Converted file
p = vlc.MediaPlayer("./Test.mp3")
p.play()
while True:
	pass