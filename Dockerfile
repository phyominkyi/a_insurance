# Use official Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy everything from your project folder into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]