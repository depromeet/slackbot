FROM ubuntu:16.04

ENV PATH /usr/local/bin:$PATH

RUN apt-get -y update
RUN apt-get install -y curl software-properties-common build-essential git apt-transport-https ca-certificates

# install python 3.6 & virtualenv
RUN add-apt-repository -y ppa:jonathonf/python-3.6 && \
    apt-get -y update && \
    apt-get install -y python3.6 python3-pip python3.6-dev python3-venv && \
    pip3 install -U pip

# install nodejs 8.10
RUN curl -L https://deb.nodesource.com/setup_8.x -o node_install.sh && \
    bash node_install.sh && \
    apt-get install -y nodejs && \
    npm install -g npm  && \
    npm install -g npx

ADD . /project
WORKDIR /project
