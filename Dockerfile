FROM python:3.6-alpine

# ADD <source> <destination>, Adds the current directory to /app in the container
COPY . /app

#install requirements 
RUN pip install -r /app/requirements.txt

# Run the web app as the main process
CMD ["python", "/app/app2.py"]
