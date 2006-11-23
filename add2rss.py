import os
import sys
import pickle
import datetime

import PyRSS2Gen # by Andrew Dalke

if len(sys.argv)!=2:
    print "Usage: add2rss.py newprogname"
    sys.exit(1)

# Find info on the new program
inputfile = open(os.path.join("data","l4c.txt"), "r")
header = inputfile.next()
foundprog = False
for line in inputfile:
    temp = line.split("\t")
    if temp[0]==sys.argv[1]:
        foundprog = temp
        break
if not foundprog:
    print "Couldn't find a program called %s" % sys.argv[1]
    sys.exit(1)

# Load the previous list
try:
    picklefile = open(os.path.join("rss", "latestadditions.pickle"), "r")
    items = pickle.load(picklefile)
    picklefile.close()
except IOError: # If you wipe latestadditions.pickle
    items = []

# Add the new item
newitem = PyRSS2Gen.RSSItem(
         title = foundprog[0],
         link = foundprog[1],
         description = foundprog[6] + "\n" + 
            "This software is %s." % foundprog[4],
## What's a guid?                       
##         guid = PyRSS2Gen.Guid("http://www.dalkescientific.com/news/"
##                          "030906-PyRSS2Gen.html"),
         pubDate = datetime.datetime.now()
         )
## items.reverse() # Remove this in future
items = [newitem] + items

# Create the RSS
rss = PyRSS2Gen.RSS2(
    title = "New additions to Linux4Chemistry",
    link = "http://www.redbrick.dcu.ie/~noel/linux4chemistry/",
    description = "The latest additions to Linux4Chemistry, "
                  "the website of chemistry software available for Linux",
    lastBuildDate = datetime.datetime.now(),
    items = reversed(items))
rss.write_xml(open(os.path.join("rss", "l4c-rss.xml"), "w"))

print "%s added." % foundprog[0]

# Save the new list
picklefile = open(os.path.join("rss", "latestadditions.pickle"), "w")
pickle.dump(items, picklefile)
picklefile.close()
