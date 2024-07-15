FROM python:3.12

RUN apt-get update && \
    pip install --upgrade pip

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /workspace
