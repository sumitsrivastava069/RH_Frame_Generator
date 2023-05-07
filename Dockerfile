FROM python:3.9

WORKDIR /app

# Copy the source code to the working directory
COPY . .
#python -m pip install --upgrade pip
# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y libsm6 libxext6 ffmpeg

CMD python -c "from app import FrameCapture; FrameCapture('./frame/test_new.mp4')"

# Expose port 5000 for 
# EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
