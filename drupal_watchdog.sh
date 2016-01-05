#!/bin/bash
while true; do 
    echo `docker exec $1 $2 -u $3 -p$4 -h $5 $6 -e "select wid, uid, type, message, variables, severity, link, location, referer, hostname, FROM_UNIXTIME(timestamp) as timestamp from watchdog order by wid desc limit 10" -B`
    echo `date`; 
    sleep 15;
done;
