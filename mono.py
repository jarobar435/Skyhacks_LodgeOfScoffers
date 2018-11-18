import sys
import wave
import audioop

from pydub import AudioSegment
sound = AudioSegment.from_wav("/home/pgazda/Desktop/sh1-2a-test/speech-test/sbc0014.wav")
sound = sound.set_channels(1)
sound = sound.set_frame_rate(16000)
sound.export("/home/pgazda/Desktop/sbc0014Mon.wav", format="wav")
