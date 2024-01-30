FROM python:3.11.7

WORKDIR /

USER root

COPY ./yml-read.py /yml-read.py

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y sudo && \
    sudo apt-get install -y systemd && \
    sudo ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN pip install numpy && \
    pip install pyyaml && \
    pip install pandas && \
    pip install pyarrow

CMD ["python3","yml-read.py"]