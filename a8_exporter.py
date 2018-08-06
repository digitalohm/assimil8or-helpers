import os, shutil, glob

project_dir = "prst001"

source_dir = '/Users/digitalohm/Documents/Ableton/' + project_dir + ' Project/Samples/Imported'
temp_dir = "/Users/digitalohm/Documents/temp_samples"
dest_dir = "/Users/digitalohm/Documents/test_samples"

if not os.path.exists(temp_dir):
    os.mkdir(temp_dir)

if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

for root, dirnames, filenames in os.walk(source_dir):
    for file in filenames:
        (shortname, extension) = os.path.splitext(file)
        if extension == ".wav" :
            shutil.copy2(os.path.join(root,file), os.path.join(temp_dir, os.path.relpath(os.path.join(root,file),source_dir)))

for filename in os.listdir(temp_dir):
     (shortname, extension) = os.path.splitext(filename)
     if extension == ".wav" :
         prefix = project_dir + '_'
         os.rename(os.path.join(temp_dir, filename), os.path.join(temp_dir, prefix + filename))

for root, dirnames, filenames in os.walk(temp_dir):
    for file in filenames:
        (shortname, extension) = os.path.splitext(file)
        if extension == ".wav" :
            shutil.copy2(os.path.join(root,file), os.path.join(dest_dir, os.path.relpath(os.path.join(root,file),temp_dir)))

shutil.rmtree(temp_dir)
