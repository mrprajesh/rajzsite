#!/bin/sh 

TSTAMP=$(date +'%d-%b-%Y-%T')
MSG="Auto+Minor update! $TSTAMP"

GITHUB=../mrprajesh.github.io/
OUTPUTDIR=./output

if [ $# -ge 1 ]
then
  MSG="$1 - $TSTAMP"
fi

# build *html
make publish

# commit srcs
git add .
git commit -m "$MSG - main"
git push 

# cp to mrprajesh.github
#~ cp -r $OUTPUTDIR/* $GITHUB
rsync -arvh $OUTPUTDIR/ $GITHUB --delete
cd $GITHUB && git add . && git commit -m "Auto updated $MSG! - site /" && git push  #"$M"
cd -

echo $TSTAMP - Done!

