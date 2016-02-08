#`gawk` Script to colorize django log output
Tries to colorize some aspects of the django log outputs. Based on the below format.

##Format expected
 - **django.sh**

        A verbose format: `[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s`  

 - **docker_django.sh**

        A verbose format: `'[DJANGO] %(levelname)s %(asctime)s %(module)s %(name)s.%(funcName)s:%(lineno)s: %(message)`
TODO:

 - [ ] Make it more intelligent.
 - [ ] Allow for customization.

##Usage
`tail -f <log file(s)> | django.sh`

##Why this?
Truth is, we're always looking at _logs_ and _logs_ are good and _logs_ makes us feel good and _logs_ are suppose to give you some good information.   
Some times this is particularly difficult if one just uses `tail -f` to read the file *live*.   
Because of this there are different tools out there to colorized files in the terminal. It is my opinion that using gawk is always fun and clean so here it is.   
This script lets you pipe the output of tail and colorize it using *RegEx*s and `gawk`. 

##Disclaimer
This is a work in progress and feel free to suggest improvements.   
I do not intend this to become an entire application or CLI and I am not trying to accomodate all of the different types of log formats out there.  

