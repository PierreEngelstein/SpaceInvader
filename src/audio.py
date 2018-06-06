#
# This file is subject to the terms and conditions defined in
# file 'LICENSE.txt', which is part of this source code package.
#

import pyaudio
import wave

class audio(object):
    
    def __init__(self):
        self.chunk_size=1024
        self.initSoundList()
        return
    
    def playSound(self, soundLocation):
        print("Playing sound " + soundLocation)
        wf = wave.open(soundLocation, 'rb')
        p=pyaudio.PyAudio()
        stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),
                      channels=wf.getnchannels(),
                      rate=wf.getframerate(),
                      output=True)
        data=wf.readframes(self.chunk_size)
        while len(data) > 0:
                stream.write(data)
                data = wf.readframes(self.chunk_size)
        
        stream.stop_stream()
        stream.close()
        
        p.terminate()
    
    def initSoundList(self):
        self.clickSound="resources/sounds/click.wav"