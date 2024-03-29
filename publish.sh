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
git commit -m "$MSG -srcs"
git push 

# cp to mrprajesh.github
cp -r $OUTPUTDIR/* $GITHUB 
cd $GITHUB && git add . && git commit -m "$MSG! mrp*.co.in" && git push  #"$M"
cd -

echo $TSTAMP - Done!

