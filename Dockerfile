#!/bin/bash
FROM jenkins/jenkins
USER root

RUN apt-get update
RUN apt-get install sudo
RUN sudo apt install python3 -y
RUN sudo apt-get install python3-pip -y
RUN pip3 install setuptools
RUN pip3 install bumpversion

RUN pip3 install wheel
RUN pip3 install pytest
RUN pip3 install pytest-cov
RUN pip3 install twine