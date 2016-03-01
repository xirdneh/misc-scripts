#!/bin/bash

# # Reset
# Color_Off='\e[0m'       # Text Reset
# 
# # Regular Colors
# Black='\e[0;30m'        # Black
# Red='\e[0;31m'          # Red
# Green='\e[0;32m'        # Green
# Yellow='\e[0;33m'       # Yellow
# Blue='\e[0;34m'         # Blue
# Purple='\e[0;35m'       # Purple
# Cyan='\e[0;36m'         # Cyan
# White='\e[0;37m'        # White
# 
# # Bold
# BBlack='\e[1;30m'       # Black
# BRed='\e[1;31m'         # Red
# BGreen='\e[1;32m'       # Green
# BYellow='\e[1;33m'      # Yellow
# BBlue='\e[1;34m'        # Blue
# BPurple='\e[1;35m'      # Purple
# BCyan='\e[1;36m'        # Cyan
# BWhite='\e[1;37m'       # White
# 
# # Underline
# UBlack='\e[4;30m'       # Black
# URed='\e[4;31m'         # Red
# UGreen='\e[4;32m'       # Green
# UYellow='\e[4;33m'      # Yellow
# UBlue='\e[4;34m'        # Blue
# UPurple='\e[4;35m'      # Purple
# UCyan='\e[4;36m'        # Cyan
# UWhite='\e[4;37m'       # White
# 
# # Background
# On_Black='\e[40m'       # Black
# On_Red='\e[41m'         # Red
# On_Green='\e[42m'       # Green
# On_Yellow='\e[43m'      # Yellow
# On_Blue='\e[44m'        # Blue
# On_Purple='\e[45m'      # Purple
# On_Cyan='\e[46m'        # Cyan
# On_White='\e[47m'       # White
# 
# # High Intensity
# IBlack='\e[0;90m'       # Black
# IRed='\e[0;91m'         # Red
# IGreen='\e[0;92m'       # Green
# IYellow='\e[0;93m'      # Yellow
# IBlue='\e[0;94m'        # Blue
# IPurple='\e[0;95m'      # Purple
# ICyan='\e[0;96m'        # Cyan
# IWhite='\e[0;97m'       # White
# 
# # Bold High Intensity
# BIBlack='\e[1;90m'      # Black
# BIRed='\e[1;91m'        # Red
# BIGreen='\e[1;92m'      # Green
# BIYellow='\e[1;93m'     # Yellow
# BIBlue='\e[1;94m'       # Blue
# BIPurple='\e[1;95m'     # Purple
# BICyan='\e[1;96m'       # Cyan
# BIWhite='\e[1;97m'      # White
# 
# # High Intensity backgrounds
# On_IBlack='\e[0;100m'   # Black
# On_IRed='\e[0;101m'     # Red
# On_IGreen='\e[0;102m'   # Green
# On_IYellow='\e[0;103m'  # Yellow
# On_IBlue='\e[0;104m'    # Blue
# On_IPurple='\e[0;105m'  # Purple
# On_ICyan='\e[0;106m'    # Cyan
# On_IWhite='\e[0;107m'   # White

gawk '
    $1 !~ "ipdb" {
        if ($3 ~ "DJANGO")
        {
            sub(/(.*)/, "\033[4;32m[DJANGO]\033[0m", $3); 


            if ($4 == "INFO")
            {
                sub(/(.*)/, "\033[0;32m" $4 "\033[0m", $4); 
            }
            else if($4 == "DEBUG")
            {
                sub(/(.*)/, "\033[0;34m" $4 "\033[0m", $4); 
            }
            else if($4 == "WARNING")
            {
                sub(/(.*)/, "\033[0;33m" $4 "\033[0m", $4); 
            }
            else if($4 == "ERROR")
            {
                sub(/(.*)/, "\033[0;31m" $4 "\033[0m", $4); 
            }
            else if($4 == "CRITICAL")
            {
                sub(/(.*)/, "\033[0;36m" $4 "\033[0m", $4); 
            }

            #colorize class name ':' line number
            $8 = gensub(/([a-z\.\-A-Z_]+):([0-9]+)/, "[\033[38;5;32m\\1\033[0m:\033[0;96m\\2\033[0m]", "G", $8);
            #colorize date YYYY-MM-DD
            $5 = gensub(/([0-9]{4}\-[0-9]{2}\-[0-9]{2})/, "[\033[38;5;130m\\1\033[0m", "G", $5);
            #colorize time HH:MM:SS(,mmm)
            $6 = gensub(/([0-9]{2}:[0-9]{2}:[0-9]{2}(,[0-9]{3})?)/, "\033[38;5;130m\\1\033[0m]", "G", $6);
        }
        if ($1 ~ "DJANGO")
        {
            sub(/(.*)/, "\033[4;32m[DJANGO]\033[0m", $1); 

            if ($2 == "INFO")
            {
                sub(/(.*)/, "\033[0;32m" $2 "\033[0m", $2); 
            }
            else if($2 == "DEBUG")
            {
                sub(/(.*)/, "\033[0;34m" $2 "\033[0m", $2); 
            }
            else if($2 == "WARNING")
            {
                sub(/(.*)/, "\033[0;33m" $2 "\033[0m", $2); 
            }
            else if($2 == "ERROR")
            {
                sub(/(.*)/, "\033[0;31m" $2 "\033[0m", $2); 
            }
            else if($2 == "CRITICAL")
            {
                sub(/(.*)/, "\033[0;36m" $2 "\033[0m", $2); 
            }
            #colorize class name ':' line number
            $6 = gensub(/([a-z\.\-A-Z_]+):([0-9]+)/, "[\033[38;5;32m\\1\033[0m:\033[0;96m\\2\033[0m]", "G", $6);
            #colorize date YYYY-MM-DD
            $3 = gensub(/([0-9]{4}\-[0-9]{2}\-[0-9]{2})/, "[\033[38;5;130m\\1\033[0m", "G", $3);
            #colorize time HH:MM:SS(,mmm)
            $4 = gensub(/([0-9]{2}:[0-9]{2}:[0-9]{2}(,[0-9]{3})?)/, "\033[38;5;130m\\1\033[0m]", "G", $4);
        }
        #colorize ip addresses.
        $0 = gensub(/[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/, "\033[32m\\0\033[0m", "g", $0);
        #colorize the URI requested
        $0 = gensub(/(GET|HEAD|POST|PUT|DELETE|TRACE|OPTIONS|CONNECT|PATCH)([^\f]*)HTTP\/[0-9]{1}\.[0-9]{1}/, "\033[0;35m\\0\033[0m", "G", $0);
        
        print $0;
    }
    '
