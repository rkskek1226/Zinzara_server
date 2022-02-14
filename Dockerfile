FROM python:3.6.5
  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y python3-dev musl-dev
RUN apt-get install -y python3-pip

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN mkdir /config

ADD /config/requirements.txt /config/
RUN pip install -r /config/requirements.txt

RUN mkdir /src;

WORKDIR /src