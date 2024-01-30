FROM python:3.11.7
ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /
USER root

RUN apt-get update && apt-get install -y \
    tzdata \
    &&  ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
    &&  apt-get clean \
    &&  rm -rf /var/lib/apt/lists/*

ENV TZ=Asia/Tokyo

RUN apt-get update \
    &&apt-get install -y sudo \
    && sudo apt-get install -y mecab \
    && sudo apt-get install -y libmecab-dev \
    && sudo apt-get install -y mecab-ipadic-utf8 \
    && sudo apt-get install -y make \
    && sudo apt install -y --reinstall build-essential \
    && sudo apt-get install -y swig \
    && sudo apt-get install -y wget \
    && sudo apt-get install -y openmpi-bin

RUN python3 -m pip install --upgrade pip \
    &&  pip install --no-cache-dir \
    black \
    jupyterlab \
    jupyterlab_code_formatter \
    jupyterlab-git \
    lckr-jupyterlab-variableinspector \
    jupyterlab_widgets \
    ipywidgets \
    import-ipynb

RUN python -m pip install --upgrade pip setuptools

RUN pip install --no-cache-dir \
    numpy \
    pandas \
    scipy \
    scikit-learn \
    pycaret \
    matplotlib \
    japanize_matplotlib \
    mlxtend \
    seaborn \
    plotly \
    requests \
    beautifulsoup4 \
    selenium \
    tqdm \
    gensim \
    janome \
    mecab-python3 \
    sentencepiece \
    accelerate \
    nltk \
    spacy \
    transformers \
    transformers[ja] \
    tensorflow[and-cuda] \
    tensorrt \
    torch \
    pytorch_lightning \
    pytorch-transformers \
    keras \
    deepspeed