FROM ubuntu:16.04

ENV PATH /usr/local/bin:$PATH

RUN apt-get -y update
RUN apt-get install -y curl software-properties-common build-essential

# install python 3.6 & virtualenv
RUN add-apt-repository -y ppa:jonathonf/python-3.6 && \
    apt-get -y update && \
    apt-get install -y python3.6 python3-pip python3.6-dev

RUN pip3 install -U pip
RUN pip3 install virtualenv

# install nodejs 8.10
RUN curl -L https://deb.nodesource.com/setup_8.x -o node_install.sh && \
    bash node_install.sh && \
    apt-get install -y nodejs

RUN npm i -g npm
