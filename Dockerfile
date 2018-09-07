FROM python:3.5.2
ENV PYTHONUNBUFFERED 1
RUN mkdir /codes
WORKDIR /codes
ADD requirements.txt /codes/
RUN pip install -r requirements.txt
ADD . /codes/
