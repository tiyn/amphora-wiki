FROM python:3

MAINTAINER tiyn tiyn@mail-mk.eu

COPY src /wiki

WORKDIR /wiki

RUN pip3 install -r requirements.txt

VOLUME /wiki/templates/entry

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
