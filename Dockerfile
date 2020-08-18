FROM python:3.8.5-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN mkdir /code
WORKDIR /code

RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

COPY run_web.sh /run_web.sh
RUN chmod +x /run_web.sh

ENTRYPOINT "/run_web.sh"