import wave
import contextlib

## The following function formats a number so that it has leading 0s as needed for the sample start/end values
def formatnumber(format_me):
    if len(format_me) < 8:
        return format_me.zfill(8 - len(format_me) + len(format_me))

sample_name = 'loop001.wav'

## The below psuedo voltage table is for the XOR NerdSeq starting at note C-4 and moving up per note
vt_nerdseq_001 = ['+4.56', '+4.48', '+4.39', '+4.31', '+4.23', '+4.14', '+4.04', '-5.00']

with contextlib.closing(wave.open(sample_name,'r')) as f:
  frames = f.getnframes()
  rate = f.getframerate()
  length = frames / float(rate)
  sample_length = int(round(length * frames))
  division = int(round(frames/8))

count = 0
part = 0

while (count < 8):
    print('Zone ' + str((count+1)) + ':')
    print('  Sample : ' + sample_name)
    print('  SampleStart : ' + formatnumber(str(part)))
    print('  SampleEnd : ' + formatnumber(str(part + division)))
    print('  MinVoltage : ' + vt_nerdseq_001[count])
    part = (part + division + 1)
    count = count + 1
