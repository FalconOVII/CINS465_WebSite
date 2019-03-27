FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip3 install -r requirements.txt

RUN mkdir /mysite
WORKDIR /mysite
COPY ./mysite /mysite

RUN adduser -D user
USER user
