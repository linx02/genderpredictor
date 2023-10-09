FROM gitpod/workspace-full

RUN sudo apt-get update && sudo apt-get install -y python3.10 python3-pip
RUN sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
RUN python3.10 -m pip install --upgrade pip