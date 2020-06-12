FROM ubuntu

MAINTAINER Tiyn tiyn@martenkante.eu

RUN apt-get update

RUN apt-get install python3 python3-pip -y

COPY src /wiki

WORKDIR /wiki

RUN pip3 install -r requirements.txt

VOLUME /wiki/templates/entry

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
