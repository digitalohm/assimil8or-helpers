# Assimil8or Helpers

Scripts I'm using while working with the Rossum-Electro Assimil8or.  The idea is to evolve the scripts based on my own workflow with the goal of focusing on music rather than anything else while I'm working on the modular.  If I can reduce some of the more tedious and repetitive tasks, then I can hopefully spend creative focus on music rather than configuration.

# Preset Template

The prst002.yml file is meant to be an ongoing evolution of a preset template that allows me to quickly dial in the values I like to use when working with the module.  This can save some time based on perferred cv mappings etc.  The other benefit I realized was the ability to preview samples on a computer, and place them in the template so they are loaded at the module, rather than previewing samples, copying them onto the microsd and turning the knob to select them.

# Slicer

The idea is a simple script that spits out preformatted text that divides a sample into 8 equal lengths (some precision lost from rounding).  I created this so that I could more easily divide zones and then fine tune the start and stop settings at the module.  It currently outputs the voltage table associated with the XOR NerdSeq that maps C-4 thru G-4 to each Zone 8 thru 1 (in that order).  It would be neat if the community would add more voltage tables for their specific sequencers and workflows.

![alt tag](https://i.imgur.com/T0tSEb5l.png "Slicer Output")

# Exporter

This script came about as I was previewing samples in Ableton.  I really like the drum rack when working with samples, it allows me to create and preview combinations of samples in a rather rapid way.  After doing this, I wanted to be able to export the files for use on the assimil8or.  The workflow as of now is to create a drum rack in an empty ableton project, save it with the name prstXXX (whatever preset I'm making), then collect and save.  From there the python script with some edited variables will copy the .wav samples (you can't do this with Ableton's punk ass aif format) into a temp directory, rename them so they have the prefix prstXXX_ and then outputs them to a directory.  The script in this repo is setup kind of generic, but on my own system I have the dest_dir the microsd card.

![alt tag](https://i.imgur.com/z2Q9F0Kh.png "Exporter Output")

# Thanks

Thanks to Gimber for allowing me to ping ideas off him and formula corrections.

Thanks to Rossum Electro for making kewl modules, and special thanks to Marco at Rossum for putting up with my constant support requests :D

The code was adapated from this stack answer https://stackoverflow.com/a/40652047
