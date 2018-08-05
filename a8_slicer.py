import wave
import contextlib

audiofile = 'Seraphim.wav'

with contextlib.closing(wave.open(audiofile,'r')) as f:
  frames = f.getnframes()
  rate = f.getframerate()
  length = frames / float(rate)
  sample_length = int(round(length * frames))
  division = int(round(sample_length/8))
  print(sample_length)
  print(division)

count = 0
part = 0

while (count < 8):
    print('Zone ' + str((count+1)) + ':')
    print('  Sample : ' + audiofile)
    print('  SampleStart : ' + str(part))
    print('  SampleEnd : ' + str(part + division))
    #print(part, (part + division)
    part = (part + division + 1)
    count = count + 1
