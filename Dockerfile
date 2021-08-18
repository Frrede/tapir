FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt update -y && apt install -y libldap2-dev libsasl2-dev

RUN pip install poetry black
