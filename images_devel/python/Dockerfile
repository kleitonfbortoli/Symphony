# set base image (host OS)
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt /app

# install dependencies
RUN pip install -r requirements.txt
RUN mv /start-reload.sh /start.sh