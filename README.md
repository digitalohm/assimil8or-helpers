# Assimil8or Helpers

Scripts I'm using while working with the Rossum-Electro Assimil8or.  The idea is to evolve the scripts based on my own workflow with the goal of focusing on music rather than anything else while I'm working on the modular.  If I can reduce some of the more tedious and repetitive tasks, then I can hopefully spend creative focus on music rather than configuration.

# Preset Template

The prst002.yml file is meant to be an ongoing evolution of a preset template that allows me to quickly dial in the values I like to use when working with the module.  This can save some time based on perferred cv mappings etc.  The other benefit I realized was the ability to preview samples on a computer, and place them in the template so they are loaded at the module, rather than previewing samples, copying them onto the microsd and turning the knob to select them.  Initially this was kind of the only reason I made a repo, to hold templates and keep track of changes...but then see below for what happened...

# Slicer

The idea is a simple script that spits out preformatted text that divides a sample into 8 equal lengths (some precision lost from rounding).  I created this so that I could more easily divide zones and then fine tune the start and stop settings at the module.  It currently outputs the voltage table associated with the XOR NerdSeq that maps C-4 thru G-4 to each Zone 8 thru 1 (in that order).  It would be neat if the community would add more voltage tables for their specific sequencers and workflows.

![alt tag](https://i.imgur.com/T0tSEb5h.png "Slicer Output")

# Exporter

This script came about as I was previewing samples in Ableton.  I really like the drum rack when working with samples, it allows me to create and preview combinations of samples in a rather rapid way.  After doing this, I wanted to be able to export the files for use on the assimil8or.  The workflow as of now is to create a drum rack in an empty ableton project, save the project with the name prstXXX (whatever preset I'm making), then collect and save.  From there the python script with some edited variables will copy the .wav samples (you can't do this with Ableton's punk ass aif format) into a temp directory, rename them so they have the prefix prstXXX_ and then outputs them to a directory.  During this process the exporter will create 8 sub directories for use with the Generator (see below).

To use you'll need to update the project_dir, source_dir, temp_dir and dest_dir variables.  For example when I save my ableton projects that I'm using for this task, I save them as: "prst00X Project" so you can see that I've made the variables to match.  If your folder containing the samples is /Users/you/kewlPreset then use that.  The project_dir is only for string building so if you update the other 3 it shouldn't matter.

![alt tag](https://i.imgur.com/p2FHeZ9h.png "Exporter Output")

![alt tag](https://i.imgur.com/aehGq34h.png "Sub Directory Example")

# Generator

So this happened, after I finished up with the exporter.  I realized there were still some tedious manual processes that I wanted to eliminate so this is the beginning of that.  The exporter creates sub directories in the destination (see above).  Each of these sub directories represent a channel on the a8.  Simply drag and drop the files exported from the exporter and then run the Generator for the beginnings of a workable .yml file.  You can also bypass the exporter part and just create the directory sturcture and drag and drop samples into them.

To use: execute the script with the -p and -d parameters, like so `python3 a8_generator.py -p prst006 -d /Users/digitalohm/Documents` the -p or --preset parameter tells the script what preset I'm wanting to work on.  The -d or --directory parameter gives the directory path for where I have the preset folders.  This will also be the path where the final results are written to.

![alt tag](https://i.imgur.com/u6RQ0kVh.png "Generator Sub Dir")

# Thanks

Thanks to Gimber and IOManip for letting me constantly ping ideas about this, workflows and formulas.  Many thanks for their corrections :D

Thanks to Rossum Electro for making kewl modules, and special thanks to Marco at Rossum for putting up with my constant support requests :D

Most of the code was adapated from various solutions on stackexchange.  The developer community is great
