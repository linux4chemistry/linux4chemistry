Find the GPL:
grep -i gpl *.html | grep -v -i gplot

Check for updates:
rm -r oldpages 
rm fixednewpages/* fixedoldpages/*
mv newpages oldpages
mkdir newpages
python getpages.py
python comparepages.py
diff fixednewpages fixedoldpages > diff.txt
gvim diff.txt
