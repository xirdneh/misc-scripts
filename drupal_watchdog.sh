#!/bin/bash
while true; do 
    echo `docker exec $1 mysql -u $2 -p$3 -h $4 $5 -e "select wid, uid, type, message, variables, severity, link, location, referer, hostname, FROM_UNIXTIME(timestamp) as timestamp from watchdog order by wid desc limit 10" -B`
    echo `date`; 
    sleep 15;
done;
