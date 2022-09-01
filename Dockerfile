FROM python:3

RUN mkdir -p /usr/src/Inforce_python_task
WORKDIR /usr/src/Inforce_python_task

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/Inforce_python_task
