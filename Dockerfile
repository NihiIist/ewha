FROM python:3.8-slim-buster

WORKDIR /app
COPY . /app/
RUN pip install pytest

CMD [ "python", "main.py"]
