FROM python:3.5
MAINTAINER Chester Wen <wenqs27@gmail.com>
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
