docker-compose -f ../portal/docker-compose-http.yml run  --rm -d --service-ports worker && \
    docker-compose -f ../portal/docker-compose-http.yml run --rm --service-ports django python -m ipdb manage.py runserver 0.0.0.0:8000 | ~/projects/misc_scripts/awk/colorized/django/docker_django.sh 
