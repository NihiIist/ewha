FROM python:3.8-slim-buster

WORKDIR /app
COPY . /app/

CMD [ "python", "main.py"]
