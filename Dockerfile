# Use an official Python runtime as a parent image
FROM python:3.12.0-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app

# Expose port 8000 for the application
EXPOSE 8000

# Set the command to start the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


# To build Docker
# docker build -t zania_chatbot .
# To run docker
# docker run -p 3000:8000 -d zania_chatbot




















# FROM python:3.7-slim

# LABEL maintainer="Shamil Kayanolil"

# ENV DOCKER=true
# COPY pyproject.toml .

# # RUN pip install --no-cache-dir --upgrade pip && \
# #     pip install --no-cache-dir poetry && \
# #     poetry install

# # RUN apt-get update
# COPY requirements.txt .
# # RUN pip install --no-cache-dir uvicorn==0.18.2
# RUN pip install --no-cache-dir -r requirements.txt
# RUN apt-get update
# COPY . .
# EXPOSE 8000
# # RUN ls -l
# # CMD ["poetry", "run", "hypercorn", "/app/main:app", "--bind", "0.0.0.0:8000", "--reload"]
# # CMD ["poetry", "run", "hypercorn", "app/main:app", "--bind", "0.0.0.0:8000", "--reload"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]