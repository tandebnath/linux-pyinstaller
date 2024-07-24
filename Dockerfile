# Use the official Ubuntu 22.04 image as the base
FROM ubuntu:22.04

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary tools and add deadsnakes PPA for Python 3.12
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.12 python3.12-venv python3.12-dev python3.12-distutils build-essential curl

# Install pip for Python 3.12
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12

# Install PyInstaller
RUN python3.12 -m pip install pyinstaller

# Set the working directory
WORKDIR /app

# Copy the project files to the working directory
COPY . .

# Install Python dependencies, ignoring already installed packages
RUN python3.12 -m pip install --ignore-installed -r requirements.txt

# Clean the output directory and build the executable using the .spec file
RUN rm -rf /app/dist/* && pyinstaller app.spec
