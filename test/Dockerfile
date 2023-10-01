FROM python:3.9-slim

WORKDIR /genomicsapptest

COPY . /genomicsapptest

RUN pip install --trusted-host pypi.python.org requests

ENV ENV=docker

CMD ["python", "-m", "unittest", "test_app.py"]