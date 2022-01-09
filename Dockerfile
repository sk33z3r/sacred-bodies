FROM python:3.8-slim-buster
# upgrade pip
RUN pip install --upgrade pip
# add openssh and clean
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install libjpeg-dev gcc libc-dev
# install python modules
ADD requirements.txt ./
RUN pip install -r requirements.txt
# generate the images
#ADD generate.py /sacred-bodies/
#ADD images /sacred-bodies/
# finish the container
WORKDIR /sacred-bodies
CMD ["bash"]