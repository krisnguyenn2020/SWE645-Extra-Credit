# Base image
FROM python:3.12.0b3-slim-bookworm

# Create app directory
RUN mkdir /app

# Set app directory as working directory
WORKDIR /app

# Set environment variables
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Update linux packages
RUN apt-get update && apt-get install -y libpq-dev

# Copy entire project folder to app folder
COPY . /app

# Upgrade python package installer
RUN pip install --upgrade pip

# Install django project dependencies
RUN pip install -r requirements.txt


# Expose port for application
EXPOSE 8000

# Command to run application
CMD [ "python3", "manage.py",  "runserver", "0.0.0.0:8000"]
