import wave
import contextlib

sample_name = 'loop001.wav'

## The below psuedo voltage table is for the XOR NerdSeq starting at note C-4 and moving up per note
vt_nerdseq_001 = ['+4.56', '+4.48', '+4.39', '+4.31', '+4.23', '+4.14', '+4.04', '-5.00']

with contextlib.closing(wave.open(sample_name,'r')) as f:
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
    print('  Sample : ' + sample_name)
    print('  SampleStart : ' + str(part))
    print('  SampleEnd : ' + str(part + division))
    print('  MinVoltage : ' + vt_nerdseq_001[count])
    part = (part + division + 1)
    count = count + 1
