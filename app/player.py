from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio

class Sound:
    def __init__(self, filename):
        self.sound = AudioSegment.from_mp3(filename)

    def play(self):
        self.playback = _play_with_simpleaudio(self.sound)
    
    def stop(self):
        self.playback.stop()

