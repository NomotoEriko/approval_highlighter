FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y git python3 python3-pip vim

RUN pip3 install flask
RUN pip3 install --upgrade flask
RUN pip3 install mysql-connector-python flask_cors

ENV APP_PATH=/home
WORKDIR $APP_PATH
ENV HOME $APP_PATH

CMD [ "/bin/sh" ]
