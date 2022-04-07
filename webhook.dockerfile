FROM centos:7
MAINTAINER Tom

WORKDIR /app
ADD . /app

RUN yum -y install epel-release
RUN yum -y install python3
RUN pip3 install --upgrade pip
RUN pip3 install requests flask


EXPOSE 5001

CMD ["python3", "webhook_LINE.py"]
