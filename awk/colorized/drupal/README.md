#`gawk` Script to colorize drupal log output
Tries to colorize some aspects of the drupal logs, more specifically php and nginx logs.

##Format expected
Log outputs of `supervisord.log`, `php5-fpm.log`, `nginx-access.log` & `nginx-error.log`
TODO:
 - [ ] Support more formats.

##Usage
`tail -f <log file(s)> | drupal.sh`

##Why this?
Truth is, we're always looking at _logs_ and _logs_ are good and _logs_ makes us feel good and _logs_ are suppose to give you some good information.   
Some times this is particularly difficult if one just uses `tail -f` to read the file *live*.   
Because of this there are different tools out there to colorized files in the terminal. It is my opinion that using gawk is always fun and clean so here it is.  

##Disclaimer
This is a work in progress and feel free to suggest improvements.   
I do not intend this to become an entire application or CLI and I am not trying to accomodate all of the different types of log formats out there.  

