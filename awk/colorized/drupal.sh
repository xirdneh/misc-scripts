#!/bin/bash

gawk '
    /==>/ { 
        sub(/^==>/, "\033[33m==>", $0)
        sub(/<==$/, "<==\033[0m", $0)
        print;
        next
    } 
    1 {
        if ($3 == "[error]" || $3 == "ERROR" || $3 == "CRIT")
        { 
            sub(/(.*)/, "\033[1;31m" $3 "\033[0m", $3); 
        }
        else if ($3 == "[warning]" || $3 == "WARN" || $3 == "WARNING")
        { 
            sub(/(.*)/, "\033[1;33m" $3 "\033[0m", $3);
        } 
        else if ($3 == "[info]" || $3 == "NOTICE:" || $3 == "INFO")
        { 
            sub(/(.*)/, "\033[1;34m" $3 "\033[0m", $3);
        }
        $0 = gensub(/[0-9]{1,3}.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/, "\033[32m\\0\033[0m", "g", $0);
        $0 = gensub(/(GET|HEAD|POST|PUT|DELETE|TRACE|OPTIONS|CONNECT|PATCH)([^\f]*)HTTP\/[0-9]{1}\.[0-9]{1}/, "\033[4;35m\\0\033[0m", "G", $0);
        print $0;
    }
    '
