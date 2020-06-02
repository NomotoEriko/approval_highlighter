FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y git python3 python3-pip vim

RUN pip3 install flask &&\
  pip3 install --upgrade flask&&\
  pip3 install torch==1.5.0+cpu torchvision==0.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html &&\
  pip3 install mysql-connector-python flask_cors jupyterlab transformers mecab-python3 ipywidgets &&\
  jupyter nbextension enable --py widgetsnbextension

ENV APP_PATH=/home
WORKDIR $APP_PATH
ENV HOME $APP_PATH

CMD [ "/bin/sh" ]
