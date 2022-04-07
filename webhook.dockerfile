FROM python
MAINTAINER Tom

WORKDIR /app
ADD . /app

RUN pip3 install requests flask

#RUN yum install -y wget

EXPOSE 5001

CMD ["python3", "webhook_LINE.py"]
