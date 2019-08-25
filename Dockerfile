FROM python:latest
WORKDIR /code
COPY . .
RUN apt-get install libjpeg-dev zlib1g-dev && pip install -r requirements.txt
# ENTRYPOINT ["python3", "genThumbnail/manage.py", "runserver"]