#!/usr/bin/python


# import cgitb; cgitb.enable() # For traceback information

import cgi
form = cgi.FieldStorage()
import datetime
now = datetime.datetime.now()

if form.keys():
    log = open("tmp.txt","a")
    print >> log, "%s %s: " % (form.getfirst("state"),now.strftime("%H:%M:%S %d-%B-%Y")),
    if form.has_key('license'):
        lics = form.getlist('license')
        ans = []
        for lic in lics:
            ans.append({'Open Source':'O','Freeware':'F','Free for academics':'A','Shareware':'S','Commercial':'C'}[lic])
        print >> log, "%s=%s" % ('license',"".join(ans)),
    if form.has_key('category'):
        print >> log, "category=%s" % (form.getfirst('category')) ,
    print >> log, ""
    log.close()

abbrev = {'MD':'Molecular Dynamics','Viewer':"3D Viewer","QM":"Quantum Mechanics","Rxn":"Reactions","Draw":"2D Draw",
          'Xtal':'Crystallography',"NMR":"NMR","Cheminf":"Cheminformatics","MM":"Molecular Mechanics",
          'Dock':'Docking','Thermo':'Thermodynamics','MS':"Mass Spectrometry","Electrochemistry":"Electrochemistry",
          'Education':'Education'}
b = [(y,x) for (x,y) in abbrev.iteritems()]
b.sort()

print """Content-Type: text/html

                <html>
                        <head>
                                <link rel="shortcut icon" href="favicon.ico">
                                <meta name="keywords" content="structure, formula, computational, kinetic, simulation, chemistry, chemical, linux, software,
programs, links, molecular modeling, molecular modelling, visualization, molecular, draw, sketch, graphics, calculations, quantum, mechanic, dynamic"/>

                                <meta name="description" content="The most up-to-date linux software (over 300) for chemistry including molecular modeling, graphics, visualization, molecular and quantum mechanic, dynamic, computational chemistry and drug discovery software"/>

                                <title>Linux4Chemistry - Linux software for chemistry: molecular modeling,
visualization, graphic, quantum mechanic, dynamic, kinetic, simulation</title>

                                <link rel="stylesheet" type="text/css" href="style.css" media="all"/>
                                <script language="javascript">
                                    <!--
                                    function clickAll (form) {
                                        for (i = 0; i < form.license.length; i++) {
                                            form.license[i].checked = true;
                                            }
                                        }
                                    function clickNone (form) {
                                        for (i = 0; i < form.license.length; i++) {
                                            form.license[i].checked = false;
                                            }
                                        }
                                    //-->
                                </script>
                        </head>
                        <body bgcolor="#f0f0f8">

<br />

<table width="95%" align="center">
<tr>
<td><img src="logo_200x305.png" alt="Welcome to Linux4Chemistry"/></td>
<td>
<h1 style="{text-align:center; font-family:Arial}">Linux4Chemistry</h1>
<table align="center" cellpadding="5%">
<tr align="center">
        <td></td>
        <td><img src="opensource_big.png" name="opensource" align="bottom" border="0"/></td>
        <td><img src="freeware_big.png" NAME="freeware" align="bottom" border="0"/></td>
        <td><img src="academic_big.png" name="academic" align="bottom" border="0"/></td>
        <td><IMG SRC="shareware_big.png" align="bottom" border="0"/></td>
        <td><IMG SRC="commercial_big.png" align="bottom" border="0"/></td>
        <td></td>
</tr>
<tr>
        <td></td>
        <td>Open Source</td>
        <td>Freeware</td>
        <td>Free for academics</td>
        <td>Shareware</td>
        <td>Commercial</td>
        <td><font size="-1"><a href="definition.html">[Explain]</a></font></td>
</tr>
<form action="http://www.redbrick.dcu.ie/~noel/linux4chemistry/linux4chemistry.py" method="post">
<tr>
<td>
<input type="button" name="selectall" value="All" onClick="clickAll(this.form)"/>
</td>
<input type="hidden" name="state" value="0"/>
"""


lic = form.getlist("license")
for name in ['Open Source','Freeware','Free for academics','Shareware','Commercial']:
    print """<td align="center"><input type="checkbox" name="license" value="%s" """ % name
    if len(lic)==0 or name in lic:
        print """checked="True" """,
    print "/></td>"

print """
<td>
<input type="button" name="selectnone" value="None" onClick="clickNone(this.form)"/>
</td>
</tr>
<tr>
<td></td>
<td colspan="5" align="center">
<select name="category">
"""

cat = form.getvalue('category',"all")
for k,v in [('All categories',"all")]+b+[('Other categories',"other")]:
    print """<option value="%s" """ % v
    if cat==v:
        print """selected="True" """
    print ">%s</option>" % k

print """
</select>
"""
#and&nbsp;<select name="category2">
#"""

#cat_b = form.getvalue('category2',"all")
#for k,v in [('All categories',"all")]+b+[('Other categories',"other")]:
#    print """<option value="%s" """ % v
#    if cat_b==v:
#        print """selected="True" """
#    print ">%s</option>" % k

print """
</select>&nbsp;<input type="submit" value="Search"/></td>
</tr>
</form>
</table>
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

<p>
Linux4Chemistry is maintained by <a href="http://www.redbrick.dcu.ie/~noel">Noel O'Boyle</a>.
Original maintainer (2001-2005) is Nikodem Kuznik.
To add a program or leave a comment, click <a href="leavecomment.html">here</a>.
Keep informed of new entries with our RSS feed. <a href="l4c-rss.xml"><img src="feed-icon-14x14.png" alt="L4C feed" border="0" /></a> Keep up to date with the CCL list with this unofficial RSS feed. <a href="http://publishious.org/site_media/RSS/ccl.rss"><img src="feed-icon-14x14.png" alt="CCL feed" border="0" /></a>
</p>


<br/>
"""

print "<ul>"
results = 0
onlyopensource = form.getlist("license")==["Open Source"]
NAME, WEB, CAT, OTHERCAT, LIC, LANG, DESC = range(7)
input = open("l4c.txt","r")
header = input.next()
for line in input:
    temp = line.strip().split("\t")

    thiscat = [x.strip() for x in temp[CAT].split(",")]
    # if (len(lic)==0 or temp[5] in form.getlist("license")) and ( (cat=="all" and cat_b=="all") or (cat in thiscat and cat_b in thiscat) or (thiscat==[''] and cat=="other" and cat_b=="other") or (cat_b=="all" and (cat in thiscat or (thiscat==[''] and cat=="other"))) or (cat=="all" and (cat_b in thiscat or (thiscat==[''] and cat_b=="other")))):
    if (len(lic)==0 or temp[LIC] in form.getlist("license")) and (cat=="all" or cat in thiscat or (thiscat==[''] and cat=="other")):
        results += 1
        print """<li><table width="97%%"><tr><td><strong><a href="%s">%s</a></strong>""" % (temp[WEB],temp[NAME])
        print """&nbsp;<img src="%s"/>""" % {"Open Source":"opensource.png",
    					 "Freeware":"freeware.png",
    					 "Free for academics":"academic.png",
    					 "Shareware":"shareware.png",
    					 "Commercial":"commercial.png"}[temp[LIC]]
        t = []
        if temp[CAT]:
            for k in thiscat:
                t.append(abbrev[k])
        if temp[OTHERCAT]:
            for k in [x.strip() for x in temp[OTHERCAT].split(",")]:
                t.append(k)
        if t:
            print "<tt>"+", ".join(t)+"</tt>"
        print '</td><td align="right"><tt>%s</tt>' % temp[LANG]
	   
        print "</td></tr></table>"
        print """<ul><li><p style="text-align:justify">%s</p></li></ul></li>""" % temp[DESC]

input.close()

if results==0:
    print """<p align="center">No results found</p>"""
else:
    print """<p align="center">%d results found</p>""" % results
    print "</ul>"

print "</body></html>"
