FROM python:3.7.2-stretch 

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
 
ONBUILD COPY requirements.txt /usr/src/app/
ONBUILD RUN pip install --no-cache-dir -r requirements.txt
 
ONBUILD COPY . /usr/src/app