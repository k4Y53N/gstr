FROM ubuntu:22.04 AS base

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update -y  && \
    apt install -y --no-install-recommends \
        libgstreamer1.0-dev \
        libgstreamer-plugins-base1.0-dev \
        libgstreamer-plugins-bad1.0-dev \
        gstreamer1.0-plugins-base \
        gstreamer1.0-plugins-good \
        gstreamer1.0-plugins-bad \
        gstreamer1.0-plugins-ugly \
        gstreamer1.0-libav \
        gstreamer1.0-tools \
        gstreamer1.0-rtsp

RUN rm -rf /var/lib/apt/lists/*


FROM base AS release

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update -y  && \
    apt install -y --no-install-recommends \
        python3-dev \
        python3-pip && \
    pip3 install --upgrade pip

RUN rm -rf /var/lib/apt/lists/* && \
    pip3 cache purge

WORKDIR /app/gstr/

COPY setup.py ./setup.py
COPY gstr/ ./gstr/
RUN pip3 install -e /app/gstr


ENTRYPOINT [ "/bin/bash" ]