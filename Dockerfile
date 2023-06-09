FROM python:3.9

WORKDIR /app

# Copy the source code to the working directory
COPY --chmod=777 . .

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y libsm6 libxext6 ffmpeg



RUN chmod -R 0777 /app
#VOLUME /app/storage/Frame
RUN chgrp -R 0 /app/storage/frameprocessorstorage && chmod -R g+rwX /app/storage/frameprocessorstorage
# Start the application
CMD ["python", "app.py"]
