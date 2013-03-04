#!/usr/bin/python

import cgitb; cgitb.enable()
import cgi

print "Content-Type: text/html"
print """
<html>
<head>
 <title>Comment page for Linux4Chemistry</title>
 <link rel="stylesheet" type="text/css" href="style.css" media="all"/>
</head>
<body bgcolor="#f0f0f8">
<br />

<table width="60%" align="center">
<tr>
<td><img src="logo_200x305.png" alt="Welcome to Linux4Chemistry"/></td>
<td align="right">
<h1 style="{text-align:center; font-family:Arial}"><a href="linux4chemistry.py?state=0">Linux4Chemistry</a></h1>
</td>
<td align="center">
<p><a href="http://www.vlib.org" target="_blank"><img src="http://vlib.org/VL.gif" alt="WWW Virtual Library" border="0" align="center"></a></p>
<strong>
<font face="Arial" size="-1">
<a href="http://www.liv.ac.uk/Chemistry/Links/links.html">Chemistry Section</a><br/>
of the <a href="http://www.vlib.org">WWW Virtual Library</a>
</font>
</strong>
</td>
</tr>
</table>
"""

message = cgi.FieldStorage().getlist("comment")
if not message:
    print """
<table width="80%" align="center">
<tr><td>
<p>To send the editors comments, updates or information on new programs, send an email to the gmail address baoilleach, or ...</p>
<ul><li><p>Fill in the box below</p></li>
<li><p>To avoid spam, any message that does not contain the word <span class="l4c">Linux4Chemistry</span> will be not be forwarded to the editor</p></li>
<li><p>Please include your email address</p></li>
<li><p>Click "Leave Comment"</p></li>
</ul>
</p>
</td></tr>
<tr><td align="center">
<form name="form" action="http://www.redbrick.dcu.ie/~noel/linux4chemistry/leavecomment.py" method="post">
<textarea name="comment" cols="80" rows="10">
</textarea>
</td></tr>
<tr><td align="center">
<input type="submit" value="Leave Comment"/>
</td></tr>
</form>
</table>
"""
else: # Email the comment
    if message[0].lower().find("linux4chemistry")>=0: # Is it a SPAM bot?
        import smtplib
        server = smtplib.SMTP("stumail.dcu.ie")
        server.sendmail("noel@redbrick.dcu.ie","l4c-devel@googlegroups.com","From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % ("noel@redbrick.dcu.ie","l4c-devel@googlegroups.com","Linux4Chemistry comment",message[0]))
        print """
    <p align="center">Thanks for helping to keep <span class="l4c">Linux4Chemistry</span> up to date.</p>
    <p align="center"><a href="linux4chemistry.py?state=0">Back to main page.</a></p>
    """
    else: # If it's a SPAM bot
        print """
    <p align="center">Sorry for the inconvenience, but since you didn't include the word <span class="l4c">Linux4Chemistry</span> in your comment, I have to assume that your message was spam. If not, please try again (press the Back button on your browser and you can edit your message) or send me an email.</p>
    <p align="center"><a href="linux4chemistry.py?state=0">Back to main page.</a></p>
    """

print """
</body>
</html>
"""
