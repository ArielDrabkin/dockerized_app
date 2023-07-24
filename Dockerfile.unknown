FROM python:3.8

WORKDIR /opt

ADD dockerized_app/ /opt/

RUN pip install -r /opt/requirements.txt

ENTRYPOINT ["python", "/opt/app.py"]