FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY . /code

CMD ["python","main.py"]