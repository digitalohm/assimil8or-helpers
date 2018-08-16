import math, argparse

## Using the parser for command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--original', required=True, help='The original bpm from the source file')
parser.add_argument('-t', '--target', required=True, help='The target bpm you want to pitch up or down to')
args = vars(parser.parse_args())

from math import log
original_bpm = float(args['original'])
adjusted_bpm = float(args['target'])
semitones = (12 * log(adjusted_bpm/original_bpm)/log(2))
print(semitones)
