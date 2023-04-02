# Dockerfile

# Author       : keshavah_reddy
# Github       : https://github.com/keshavah-reddy
# Date         : 29-08-2022
# Main Language: Python

# Download and import main images

# Operating system
FROM debian:latest
# Main package
FROM python:3

# Author info
LABEL MAINTAINER="https://github.com/keshavah-reddy/meow-v2"

# Working directory
WORKDIR meow-v2/
# Add files 
ADD . /meow-v2

# Installing other packages
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install php openssh-client -y
RUN pip3 install -r files/requirements.txt
RUN apt-get clean

# Main command
CMD ["python3", "meow-v2.py", "--noupdate"]

## Wanna run it own? Try following commnads:

## "sudo docker build . -t keshavah-reddy/meow-v2:latest", "sudo docker run --rm -it keshavah-reddy/meow-v2:latest"

## "sudo docker pull keshavah-reddy/meow-v2", "sudo docker run --rm -it keshavah-reddy/meow-v2"
