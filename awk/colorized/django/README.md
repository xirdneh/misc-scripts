#gawk script to colorize django log output

##Format expected
A verbose format: `[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s`  
TODO:
 - [ ] Support simpler format: `[%(levelname)s] %(message)s`

##Usage
`tail -f <log file(s)> | django.sh`

##Why this?
Truth is, we're always looking at logs and logs are good and logs makes us feel good and logs are suppose to give you some good information. Some times this is particularly difficult if one just uses `tail -f` to read the file *live*. Because of this there are different tools out there to colorized files in the terminal. It is my opinion that using gawk is always fun and clean so here it is. This script lets you pipe the output of tail and colorize it using *RegEx*s and `gawk`. 

##Disclaimer
This is a work in progress and feel free to suggest improvements.   
I do not intend this to become an entire application or CLI and I am not trying to accomodate all of the different types of log formats out there.  

