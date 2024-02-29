FROM python:3.11

WORKDIR ./docker_demo

ADD . .

RUN pip3 install -r requirements.txt

CMD ["python", "./src/main.py"]