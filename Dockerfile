FROM python:3.8

WORKDIR /opt

ADD . /opt/

RUN pip install -r /opt/requirements.txt

ENTRYPOINT ["python", "inference.py"]