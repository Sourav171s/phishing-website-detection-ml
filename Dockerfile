FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

COPY  .env .env

RUN pip install -r requirements.txt

CMD ["python","app.py"]
