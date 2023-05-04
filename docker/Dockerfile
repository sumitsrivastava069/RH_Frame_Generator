FROM docker.io/python
# By default, listen on port 8081
EXPOSE 8081/tcp


# Set the working directory in the container
WORKDIR /projects

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD [ "python", "./app.py" ]
