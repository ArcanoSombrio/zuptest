FROM debian:latest

# Define o mantenedor da imagem
LABEL maintainer="Daniel Lucas Ferreira"

# Atualizar a imagem
RUN apt-get update && apt-get upgrade -y

# Instala as dependências
RUN apt-get install -y tar build-essential \
    zlib1g-dev libncurses5-dev libgdbm-dev \
    libnss3-dev libssl-dev libsqlite3-dev \
    libreadline-dev libffi-dev curl libbz2-dev \
    git chromium chromium-l10n firefox-esr xvfb

# Instala o Python 3.8
RUN mkdir $HOME/Downloads
RUN cd $HOME/Downloads && curl -O https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tar.xz
RUN cd $HOME/Downloads && tar -xf Python-3.8.2.tar.xz
RUN cd $HOME/Downloads/Python-3.8.2 && ./configure --enable-optimizations
RUN cd $HOME/Downloads/Python-3.8.2 && make -j 4 &&  make altinstall
RUN cd $HOME/Downloads && rm -rf Python-3.8.2
RUN cd $HOME/Downloads && rm -rf Python-3.8.2.tar.xz

# Instala as bibliotecas necessárias
RUN python3.8 -m pip install selenium behave xlrd PyVirtualDisplay behave DateTime urllib3

# Clonar projeto de testes do GitHub
RUN mkdir $HOME/Documents
RUN cd $HOME/Documents && git clone https://github.com/ArcanoSombrio/zuptest.git
