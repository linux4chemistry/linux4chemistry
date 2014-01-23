import os

inputfile = open(os.path.join("data","l4c.txt"),"r")
oldname = "a"
for line in inputfile:
    name = line.split('\t')[0]
    if name.upper()<oldname.upper():
        print "Is %s > %s?" % (name, oldname)
    oldname = name
