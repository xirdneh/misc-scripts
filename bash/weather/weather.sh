#!/bin/bash
set -x
# set home and take weather as argument
LOCATION=${@:-"austin tx"}

# now call the weather
echo "http://wttr.in/$LOCATION" | sed -e 's#\ #\\ #g' | xargs curl 
