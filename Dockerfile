FROM python:3.9-slim

WORKDIR /genomicsapp

COPY . /genomicsapp

RUN pip install --trusted-host pypi.python.org uvicorn fastapi

EXPOSE 80

ENV UVICORN_CMD="uvicorn app:app --host 0.0.0.0 --port 80 --reload"

CMD ["sh", "-c", "$UVICORN_CMD"]
