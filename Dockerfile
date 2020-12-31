FROM python:3.8-slim

COPY . ./

RUN pip install Flask gunicorn

CMD gunicorn --bind :8000 app:app
