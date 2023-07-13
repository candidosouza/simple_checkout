FROM python:3.11

RUN apt update && apt install -y --no-install-recommends curl wget \
    && python -m pip install --upgrade pip

RUN useradd -ms /bin/bash python

USER python

WORKDIR /home/python/app

ENV PYTHONPATH=${PYTHONPATH}/home/python/app


CMD ["tail", "-f", "/dev/null"]