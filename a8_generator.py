import glob, os, re

vt_nerdseq_001 = ['+4.56', '+4.48', '+4.39', '+4.31', '+4.23', '+4.14', '+4.04', '-5.00']

preset = "prst003"

sample_dir = '/Users/digitalohm/Documents/' + preset

channels = []
print('Preset 1 :')
print('  Name : ' + sample_dir[len(sample_dir)-7:len(sample_dir)])
## Loop one time for directories that are not empty
for root, dirnames, filenames in os.walk(sample_dir):
    for directory in dirnames:
        if os.listdir(sample_dir + '/' + directory) :
            channels.append(directory)

#print(channels)

i = 1
for directory in channels:
    samples = []
    print('  Channel ' + str(i) + ': ')
    print('    Release :  0.8000')
    print('    LinFM : 0C 0.00')
    print('    LinAM : Off 0.00')
    print('    ZonesCV : 0B')
    print('    ZonesRT : 1')
    for root, dirnames, filenames in os.walk(sample_dir + '/' + str(i)):
        for file in filenames:
            (shortname, extension) = os.path.splitext(file)
            if len(shortname) > 47:
                samples.append(shortname[:-(len(shortname)-47)] + extension)
            else:
                samples.append(file)

    samples.sort()
    j = 0
    for sample in samples:
        #print(''.join(filter(str.isdigit, sample[7:len(sample)])))
        print('    Zone ' + str((j+1)) + ':')
        print('      Sample : ' + sample)
        print('      MinVoltage : ' + vt_nerdseq_001[j])
        j += 1
    del sample
    i += 1
