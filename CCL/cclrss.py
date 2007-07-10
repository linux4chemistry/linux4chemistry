import sys
import email
import datetime

from ftplib import FTP
from StringIO import StringIO

import PyRSS2Gen

def breakdaily(messages):
    """
    >>> import pickle
    >>> a = pickle.load(open("tmp20070105"))
    >>> len(breakdaily(a))
    1
    """
    broken = []
    message = []
    for line in messages.split("\n"):
        if line.startswith("From owner-chemistry@ccl.net"):
            broken.append("\n".join(message))
            message = []
        else:
            message.append(line)
    broken.append("\n".join(message))
    return broken[1:]

def getlatest(N):
    ftp = FTP('ftp.ccl.net')
    ftp.login('anonymous')
    ftp.cwd('/pub/chemistry/archived-messages')
    # ftp.dir()

    listoffiles = ftp.nlst()

    # Get current year
    year = datetime.datetime.now().year

    # Get N most recent messages
    messagetot = 0
    months = [str(x).zfill(2) for x in range(1, 13)]
    months.reverse()
    days = [str(x).zfill(2) for x in range(1, 32)]
    days.reverse()
    msgs = []
    

    while messagetot<N:  
        ftp.cwd(str(year))

        for month in months:
            ftp.cwd(month)
            availabledays = ftp.nlst()
            for day in [x for x in days if x in availabledays]:
                # Go thru in reverse order but exclude days that are
                # non-existent
                messages = StringIO()
                ftp.retrbinary("RETR %s" % day, messages.write)
##                pickle.dump(messages.getvalue(), open("tmp%i%s%s" % (year,month,day), "w"))
                listmsgs = breakdaily(messages.getvalue())
                print "="*24 + "\n", messages.getvalue()
                for i,msg in enumerate(listmsgs):
                    msgs.append( (year, month, day, i+1, msg) )
                messagetot += len(listmsgs)
                if messagetot>=N:
                    break
            if messagetot>=N:
                break
            ftp.cwd("..")
        ftp.cwd("..")
        year -= 1 # Continue into the previous year

    ftp.quit()
    
    return msgs

def main():
    
    print "\nStarting..."

    messages = getlatest(100)
##    outputfile = open("messages.pickle", "w")
##    pickle.dump(messages, outputfile)
##    outputfile.close()
##    import sys
##    sys.exit(1)
##    messages = pickle.load(open("messages.pickle", "r"))

    rssitems = []
    for year, month, day, id, messagemime in messages:
        msg = email.message_from_string(messagemime)
        text = ""

        for part in msg.walk():
##            print part.get_content_maintype()
##            print part.get_content_type()
            if (part.get_content_maintype()=="text" and
                part.get_content_type()=="text/plain"):
                text = part.get_payload()

        # Add the new item
        newitem = PyRSS2Gen.RSSItem(
                 title = msg['Subject'],
                 link = "http://ccl.net/cgi-bin/ccl/message-new?%d+%s+%s+%s" % (
                         year, month, day, str(id).zfill(3)),
                 description = text.replace("\n","<br/>"),
        ## What's a guid? A globally unique id...used by RSS readers
        ## to determine whether they've seen a particular news item
        ## already
                 guid = PyRSS2Gen.Guid("http://ccl.net/cgi-bin/ccl/message-new?%d+%s+%s+%s" % (
                         year, month, day, str(id).zfill(3))),
                 pubDate = msg['Date']
                 )
        rssitems.append(newitem)

    rss = PyRSS2Gen.RSS2(
        title = "CCL",
        link = "http://www.ccl.net",
        description = "RSS Feed of the world's greatest computational chemistry"
                      "mailing list, chemistry@ccl.net (the CCL list)",
        lastBuildDate = datetime.datetime.now(),
        items = rssitems)
    rss.write_xml(open("ccl-rss.xml", "w"))                
        
    print "Finishing...\n"

def test():
    import doctest
    doctest.testmod()

if __name__=="__main__":
    
    main()

    ## test()    