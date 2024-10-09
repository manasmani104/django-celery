# Dockerfile
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the Django project files
COPY . /code/

# Add entrypoint script
COPY entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh

# Command to run Django server
CMD ["/code/entrypoint.sh"]
