#!/bin/sh

dist=website

rm -r $dist
mkdir $dist

cp src/linux4chemistry.py $dist
cp src/leavecomment.py $dist
cp data/l4c.txt $dist
cp rss/l4c-rss.xml $dist
cp src/definition.html $dist
cp src/style.css $dist
cp img/*.png $dist
mkdir $dist/email
cp src/carlo_nervi.* $dist/email

cd $dist
python linux4chemistry.py | tail +3 | sed 's/name="state" value="0"/name="state" value="1"/g' > index.html
python leavecomment.py | tail +3 | sed 's/name="state" value="0"/name="state" value="1"/g' > leavecomment.html
