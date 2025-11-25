FROM python:3.14

RUN mkdir /opt/hello_world/
WORKDIR /opt/hello_world/

COPY requirements.txt .
COPY hello_world.py /opt/

EXPOSE 80

CMD [ "./hello_world" ]
