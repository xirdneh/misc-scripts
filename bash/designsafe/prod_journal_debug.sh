ssh -tt designsafe01.tacc.utexas.edu "sudo -u root /bin/journalctl -f -u designsafe" | awk '{print substr($0, index($0, $6)) }' | ~/projects/misc_scripts/awk/colorized/django/docker_django.sh 
