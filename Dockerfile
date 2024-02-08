FROM python:3.8-slim-buster

RUN pip install -U pip setuptools wheel
RUN pip install pdm

ADD hello-world.py /

CMD [ "python", "./hello-world.py" ]
