import os, shutil, glob, argparse

## Using the parser for command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--preset', required=True, help='This is the name of the preset, and the final destination folder, and prefix for fine renames')
parser.add_argument('-s', '--source_directory', required=True, help='This is the source directory that contains the samples you want to copy')
parser.add_argument('-d', '--destination_directory', required=True, help='This is the place you want to copy the files to')
args = vars(parser.parse_args())

## The project_dir variable is used just for some string manipulation below, it can be ignored if you are using a different method
project_dir = args['preset']

## The source_dir is the place where your samples are at, the temp_dir is a temporary folder for renaming the copied files, and the dest_dir is the final place for them
#source_dir = '/Users/digitalohm/Documents/Ableton/' + project_dir + ' Project/Samples/Imported'
source_dir = args['source_directory']
temp_dir = args['destination_directory'] + '/temp_samples'
dest_dir = args['destination_directory'] + '/' + project_dir

## The sub_dir variable corresponds to the channels on the assimil8or, '1' = Channel 1 etc.
sub_dir = ['1', '2', '3', '4', '5', '6', '7', '8']

## Create directories
if not os.path.exists(temp_dir):
    os.mkdir(temp_dir)

if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

i = 0
for subdirectory in sub_dir:
    if not os.path.exists(dest_dir + '/' + sub_dir[i]):
        os.mkdir(dest_dir + '/' + sub_dir[i])
        i += 1

## First copy the .wav files from the source_dir to the temp_dir
for root, dirnames, filenames in os.walk(source_dir):
    for file in filenames:
        (shortname, extension) = os.path.splitext(file)
        if extension == '.wav' :
            shutil.copy2(os.path.join(root,file), os.path.join(temp_dir, os.path.relpath(os.path.join(root,file),source_dir)))
            #print(os.path.join(temp_dir, os.path.relpath(os.path.join(root,file),source_dir)))

## Next rename the files in the temp_dir
for filename in os.listdir(temp_dir):
     (shortname, extension) = os.path.splitext(filename)
     if extension == '.wav' :
         prefix = project_dir + '_'
         if len(shortname) > 47:
             os.rename(os.path.join(temp_dir, filename), os.path.join(temp_dir, prefix + shortname[:-(len(shortname)-47)] + extension))
             #print(prefix + shortname[:-(len(shortname)-47)] + extension)
         else:
             os.rename(os.path.join(temp_dir, filename), os.path.join(temp_dir, prefix + filename))
             #print(prefix + filename)

## Finally copy the renamed files from the temp_dir to the dest_dir
for root, dirnames, filenames in os.walk(temp_dir):
    for file in filenames:
        (shortname, extension) = os.path.splitext(file)
        if extension == '.wav' :
            shutil.copy2(os.path.join(root,file), os.path.join(dest_dir, os.path.relpath(os.path.join(root,file),temp_dir)))
            #print(temp_dir)

## And remove the temp_dir
shutil.rmtree(temp_dir)
