import glob, os, re

sample_dir = "/Users/digitalohm/Documents/prst001/"
vt_nerdseq_001 = ['+4.56', '+4.48', '+4.39', '+4.31', '+4.23', '+4.14', '+4.04', '-5.00']

ch1_samples = []
for root, dirnames, filenames in os.walk(sample_dir + '/1'):
    for file in filenames:
        (shortname, extension) = os.path.splitext(file)
        ch1_samples.append(file)

if ch1_samples:
    ch1_samples.sort()
    #print(ch1_samples)

    print('Preset 1 :')
    print('  Name : ' + sample_dir[len(sample_dir)-8:len(sample_dir)-1])
    print('  Channel 1: ')
    print('    Release :  0.8000')
    print('    LinFM : 0C 0.00')
    print('    LinAM : Off 0.00')
    print('    ZonesCV : 0B')
    print('    ZonesRT : 1')

    i = 0
    for sample in ch1_samples:
        #print(''.join(filter(str.isdigit, sample[7:len(sample)])))
        print('    Zone ' + str((i+1)) + ':')
        print('      Sample : ' + sample)
        print('      MinVoltage : ' + vt_nerdseq_001[i])
        i += 1

    del sample

ch2_samples = []
for root, dirnames, filenames in os.walk(sample_dir + '/2'):
    for file in filenames:
        (shortname, extension) = os.path.splitext(file)
        ch2_samples.append(file)

if ch2_samples:
    ch2_samples.sort()
    #print(ch2_samples)

    print('  Channel 2: ')
    print('    Release :  0.8000')
    print('    LinFM : 0C 0.00')
    print('    LinAM : Off 0.00')
    print('    ZonesCV : 0B')
    print('    ZonesRT : 1')

    i = 0
    for sample in ch2_samples:
        #print(''.join(filter(str.isdigit, sample[7:len(sample)])))
        print('    Zone ' + str((i+1)) + ':')
        print('      Sample : ' + sample)
        print('      MinVoltage : ' + vt_nerdseq_001[i])
        i += 1

    del sample

ch3_samples = []
for root, dirnames, filenames in os.walk(sample_dir + '/3'):
    for file in filenames:
        (shortname, extension) = os.path.splitext(file)
        ch3_samples.append(file)

if ch3_samples:
    ch3_samples.sort()
    #print(ch3_samples)

    print('  Channel 3: ')
    print('    Release :  0.5000')
    print('    LinFM : 0C 0.00')
    print('    LinAM : Off 0.00')
    print('    ZonesCV : 0B')
    print('    ZonesRT : 1')

    i = 0
    for sample in ch3_samples:
        #print(''.join(filter(str.isdigit, sample[7:len(sample)])))
        print('    Zone ' + str((i+1)) + ':')
        print('      Sample : ' + sample)
        print('      MinVoltage : ' + vt_nerdseq_001[i])
        i += 1

    del sample
