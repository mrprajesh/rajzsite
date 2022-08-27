#!/bin/sh
#! cp _posts/template.md _posts/$(date +'%Y-%m-%d')-$1.md

DIR=content/news
FILE=$(date +'%Y-%m-%d')-new-post.md
TITLE="Edit this to a new title" # This will be the default title

if [ $# -lt 1 ]; then
  echo "Usage: ./newpost.sh title-of-the-post"
  exit 1;
fi

if [ $# -ge 1 ] # if given with 1st args (assumes 1st arg is hyphenated)
then
  FILE=$(date +'%Y-%m-%d')-"$1".md
  TITLE=$(echo "$1" | sed 's/-/\ /g') #remove hyphens
fi

if [ -f $DIR/$FILE ] #if the same file name found then, suffix with time
then
  FILE=$(date +'%Y-%m-%d-%T').md
fi

echo "Title: $TITLE"                    >> $DIR/$FILE
echo "Date: $(date +'%d-%b-%Y %T %:z')" >> $DIR/$FILE
echo "Category: News"                   >> $DIR/$FILE
echo ""                                 >> $DIR/$FILE

echo $DIR/$FILE - created!

geany $DIR/$FILE
