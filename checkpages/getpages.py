"""Finds any redirecting web pages."""
from urllib2 import urlopen,HTTPError
from httplib import BadStatusLine
import socket
socket.setdefaulttimeout(10)
from gnosis.xml.objectify import XML_Objectify
from cPickle import dump
from BeautifulSoup import BeautifulSoup

import os,string
from datetime import date

def normalise(mystring):
    """Replace punctuation with _."""
    for x in string.punctuation:
        mystring = mystring.replace(x,"_")
    return mystring


if __name__=="__main__":

    py_obj = XML_Objectify("../xml/linux4chemistry.xml")
    doc = py_obj.make_instance()

    page = {}

    now = date.today().strftime("%d-%m-%y")

    redirect_log = open("redirection.txt","a")
    ioerror_log = open("ioerror.txt","a")
    nopage_log = open("nopage.txt","a")

    list = [(i,v) for i,v in enumerate(doc.program)]

    for i,program in list:
        print "%d Checking program %s" % (i,program.name)
        href = program.href
        if not href.startswith("email/"):
            try:
                redirect = False
                a = urlopen(href)
                webpage = a.read()
                soup = BeautifulSoup(webpage)
                for meta in soup('meta'):
                    for k,v in meta.attrs:
                        if k.lower()=="http-equiv" and v.lower()=="refresh":
                            redirect = True
                        if k.lower()=="content":
                            content = v
                    if redirect:
                        redirect_to = content.split("=")[1]
                        if redirect_to.find("http:")<0: # must be relative href
                            if href[-1]=="/" or href[-1]=="\\":
                                href = href[:-1]
                            if redirect_to[0]=="/" or redirect_to[1]=="\\":
                                redirect_to = redirect_to[1:]
                            redirect_to = href+"/"+redirect_to
                        print ".............redirection to %s" % redirect_to
                        print >> redirect_log, "%s\t%s" % (program.name, now)
                        a.close()
                        a = urlopen(redirect_to)
                        webpage = a.read()
            except IOError:
                print "..................................IOError"
                print >> ioerror_log, "%s\t%s" % (program.name, now)
            except HTTPError,e:
                print "..................................HTTPError"
                print >> ioerror_log, "%s\t%s HTTPError %d" % (program.name,now,e.code)
            except BadStatusLine:
                print "..................................BadStatusLine"
                print >> ioerror_log, "%s\t%s BadStatusLine" % (program.name,now)
            except AttributeError:
                # Page does not exist so...
                # AttributeError: 'NoneType' object has no attribute 'read'
                print "............................%s does not exist" % href
                print >> nopage_log, "%s\t%s" % (program.name, now)
            except socket.timeout:
                print "..........................socket timed out"
                print >> ioerror_log, "%s\t%s (%s)" % (program.name, now, "socket timed out")
            else:
                a.close()

                output = open(os.path.join("newpages",normalise(program.name)+".html"),"w")
                output.write(webpage)
                output.close()

    redirect_log.close()
    ioerror_log.close()
    nopage_log.close()
