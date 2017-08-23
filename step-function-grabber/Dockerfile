FROM continuumio/miniconda

RUN apt-get update
RUN apt-get install -y \
    build-essential \
    curl \
    python-dev

RUN mkdir -p /code
WORKDIR /code

ADD . /code

# RUN conda install -y numpy
# RUN conda install -y llvmlite==0.17.0 -v
# RUN conda install -y numba==0.34.0 -v
# RUN conda install -y fastparquet

# RUN cp -a /opt/conda/pkgs/. /code/libs