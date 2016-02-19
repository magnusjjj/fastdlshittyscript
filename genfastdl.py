#!/usr/bin/python

# MIT licensed and open source, because my friend, when i asked him about a fastdl script for my playground server...

#anon: We do, but i cant give you that
#anon: Noone has a propper fastdl sync script, except for a few servers
#anon: its what makes them good
#anon: I dont mind sharing some lua and stuff, but i cant share the main stuff with you

import os
import re
import subprocess
import string

dir = "/home/steam/steamapps/common/GarrysModDS/garrysmod/addons/"
target = "./"
tocopy = ['maps', 'materials', 'models', 'sound', 'particles', 'resource']

# First pass, copy all the shizzle already in there

for subdir in tocopy:
        subprocess.call(("cp", "-rfv", dir+'../'+subdir, target))

# Second pass, copy all of the addon content
for subdir, dirs, files in os.walk(dir):
        for file in files:
                pathy = subdir[len(dir):]
                regex = re.search('([^/]*)/([^/]*)/(.*)',pathy+'/'+file)
                if regex:
                        addonname = regex.group(1)
                        foldertype = regex.group(2)
                        filename_simple = regex.group(3)
                        if foldertype in tocopy:
                                fromfile = foldertype+'/'+filename_simple
                                fromdir = string.rsplit(fromfile, '/', 1)[0]
                                tofile = target+'/'+fromfile
                                subprocess.call(("mkdir", "-pv", target+'/'+fromdir))
                                subprocess.call(("cp", "-fv", subdir+'/'+file, tofile))

# Third pass, bz2 up those bitches. Bitches loooove bz2
for subdir, dirs, files in os.walk(target):
        for file in files:
                fullname = subdir+'/'+file
                filename, file_extension = os.path.splitext(fullname)
                if file_extension != ".bz2":
                        if not (os.path.isfile(fullname+".bz2")):
                                subprocess.call(("bzip2", "-9v", "-k", fullname))
