FROM gitpod/workspace-full

RUN pyenv install 3.11 \
    && pyenv global 3.11

RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev