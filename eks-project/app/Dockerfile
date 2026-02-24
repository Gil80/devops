# Pick a low configuration python base image
FROM python:alpine

# tells Python to run in unbuffered mode. This means that Python will not buffer output,
# but will instead print it directly to the console.
# This is useful when running Python inside a Docker container,
# as it can help to avoid some complications when running your Python application.
# For example, if you are running a Python application that logs output to the console,
# and you want to view the logs in real time, you will need to set the PYTHONUNBUFFERED environment variable to 1.
# This will tell Python to print output directly to the console, without buffering it.
ENV PYTHONUNBUFFERED=1

# Install python3 and symlink it to python
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python

RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# create and activate virtual env
# using final folder name to avoid path issues with packages

RUN python3 -m venv /home/gil/venve
ENV VIRTUAL_ENV=/home/gil/venve
ENV PATH="/home/gil/venve/bin:$PATH"
RUN source /home/gil/venve/bin/activate

# create user without password
RUN adduser gil -D

# Create a folder app in container and work inside it
WORKDIR /home/gil/app

# Copy all the flask project files into the WORKDIR
COPY requirements.txt .

# install bash
RUN apk add --no-cache bash

# install all the requirements
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

# copies all of the files from the current directory into the Docker image
COPY . .

# exposes the port 5000 of the Docker container. This is the port that the Flask application will listen on.
EXPOSE 5000

# exexcute the flask app inside the container
CMD python3 app.py
