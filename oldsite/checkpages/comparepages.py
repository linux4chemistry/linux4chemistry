import os
from glob import glob

for folder in ["old","new"]:
    for filename in glob(os.path.join(folder+"pages","*.html")):
        file = open(filename,"r")
        output = open(os.path.join("tmppages",os.path.basename(filename)),"w")
        output.write(file.read().replace("\r","\n"))
        output.close()
        file.close()

        file = open(os.path.join("tmppages",os.path.basename(filename)),"r")
        output = open(os.path.join("fixed"+folder+"pages",os.path.basename(filename)),"w")
        for line in file:
            line.replace("\r","\n")
            ignore = ['accesse','GMT','2006','</html><!--','todaynoevent','servicenav-off',
                      'padding: 0px','aaaatrap','lycos','Monday','Tuesday','Wednesday',
                      'Thursday','Friday','Saturday','Sunday','<!-- Served by ',
                      'Registered users','before_n=new Image();','before_h=new Image();']
            dontignore = True
            for word in ignore:
                if line.find(word)>=0:
                    dontignore = False
            if dontignore:
                output.write(line)
        output.close()
        file.close()
