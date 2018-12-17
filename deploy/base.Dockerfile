FROM python:3.6-alpine3.8

LABEL MAINTAINER="Liad Magen, liad.magen@gmail.com"

ENV CFLAGS="-fPIC"

WORKDIR  /usr/local/include

RUN apk --no-cache add lapack && \
    apk --no-cache add --virtual builddeps g++ gfortran musl-dev lapack-dev gcc make && \
    # musl-dev python3-dev openblas-dev && \
    \
    wget https://mupdf.com/downloads/archive/mupdf-1.13.0-source.tar.gz -O - | tar -xz && \
    mv mupdf-1.13.0-source mupdf  && \
    cd mupdf && \
    make HAVE_X11=no HAVE_GLFW=no HAVE_GLUT=no prefix=/usr/local && \
    make HAVE_X11=no HAVE_GLFW=no HAVE_GLUT=no prefix=/usr/local install && \
    mv /usr/local/include/mupdf/thirdparty /usr/local/thirdparty

WORKDIR  /opt/app

RUN pip install numpy==1.15.4 && \
    pip install scipy==1.1.0 && \
    pip install scikit-learn==0.20 && \
    pip install pandas==0.23.4 && \
    pip install -U spacy==2.0.17.dev1  && \
    python -m spacy download en && \
    apk del builddeps     && \
    rm -rf /root/.cache
