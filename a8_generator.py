import os, shutil, glob, re, argparse, sys

## Using the parser for command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--preset", required=True, help="name of the preset")
parser.add_argument("-d", "--directory", required=True, help="location of the samples")
#Not yet implmented
parser.add_argument("-v", "--verbose", help="prints the yml configuration to stdout", action="store_true")
args = vars(parser.parse_args())

## Voltage table for the nerseq.  This is for notes C-4 through G-4 to hit Zones 8 thru 1 (in that order)
vt_nerdseq_001 = ['+4.56', '+4.48', '+4.39', '+4.31', '+4.23', '+4.14', '+4.04', '-5.00']

## This is the name of the preset which works nicely if it's the same name as your sample source folder
preset = args["preset"]

## First make sure the path to the samples is valid
if os.path.isdir(args["directory"]):
    sample_dir = args["directory"] + '/' + preset

## String building once for later use
dest_dir = args["directory"] + '/completed_' + preset

## Check if the destination directory exists, if it does, delete it and create it agian.  If not, create it!
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
else:
    shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)

## Build a list of the channel directories that are not empty, and print the beginnings of the yml
channels = []
file_path = dest_dir + '/' + preset + '.yml'
#print(file_path)
with open(file_path, 'w') as f:
    f.write('Preset 1 :\r\n')
    #print('Preset 1 :')
    f.write('  Name : ' + sample_dir[len(sample_dir)-7:len(sample_dir)]+'\r\n')
    #print('  Name : ' + sample_dir[len(sample_dir)-7:len(sample_dir)])
    ## Loop one time for directories that are not empty
    for root, dirnames, filenames in os.walk(sample_dir):
        for directory in dirnames:
            if os.listdir(sample_dir + '/' + directory):
                channels.append(directory)

    ## Next we loop through each folder from the channles[] list and print the yml
    i = 1
    for directory in channels:
        if i <= 8:
            samples = []
            f.write('  Channel ' + str(i) + ': \r\n')
            #print('  Channel ' + str(i) + ': ')
            f.write('    Release :  0.8000\r\n')
            #print('    Release :  0.8000')
            f.write('    LinFM : 0C 0.00\r\n')
            #print('    LinFM : 0C 0.00')
            f.write('    LinAM : Off 0.00\r\n')
            #print('    LinAM : Off 0.00')
            f.write('    ZonesCV : 0B\r\n')
            #print('    ZonesCV : 0B')
            f.write('    ZonesRT : 1\r\n')
            #print('    ZonesRT : 1')
            for root, dirnames, filenames in os.walk(sample_dir + '/' + str(i)):
                for file in filenames:
                    (shortname, extension) = os.path.splitext(file)
                    if extension == '.wav':
                        if len(shortname) > 47:
                            samples.append(shortname[:-(len(shortname)-47)] + extension)
                        else:
                            samples.append(file)

            samples.sort()
            j = 0
            for sample in samples:
                f.write('    Zone ' + str((j+1)) + ':\r\n')
                #print('    Zone ' + str((j+1)) + ':')
                f.write('      Sample : ' + sample + '\r\n')
                #print('      Sample : ' + sample)
                f.write('      MinVoltage : ' + vt_nerdseq_001[j] + '\r\n')
                #print('      MinVoltage : ' + vt_nerdseq_001[j])
                j += 1

            #del sample
            i += 1

    f.close()


## Finally copy the files to the completed folder which is ready for a8 use
for root, dirnames, filenames in os.walk(sample_dir):
    for file in filenames:
        (shortname, extension) = os.path.splitext(file)
        if extension == '.wav' and os.path.join(root,file) != sample_dir:
            shutil.copy2(os.path.join(root,file), os.path.join(dest_dir,file))
