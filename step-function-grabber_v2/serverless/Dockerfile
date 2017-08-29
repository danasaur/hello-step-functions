from ubuntu:16.04


RUN apt-get update && \
    apt-get install -y software-properties-common && \
    apt-add-repository ppa:ansible/ansible && \
    DEBIAN_FRONTEND=noninteractive  apt-get update  && \
    \
    \
    echo "===> Installing Ansible..."  && \
    apt-get install -y ansible  && \
    \
    \
    echo "===> Adding hosts for convenience..."  && \
    echo 'localhost' > /etc/ansible/hosts

RUN apt-get install -y \
    python-pip \
    python-dev \
    build-essential 

RUN pip install --upgrade pip 
RUN pip install boto3

ENV ANSIBLE_GATHERING smart
ENV ANSIBLE_HOST_KEY_CHECKING false
ENV ANSIBLE_RETRY_FILES_ENABLED false
ENV ANSIBLE_SSH_PIPELINING True
ENV PATH /ansible/bin:$PATH
ENV PYTHONPATH /ansible/lib

# default command: display Ansible version
CMD ["/bin/bash"]

RUN mkdir -p /code/
WORKDIR /code

ADD . /code