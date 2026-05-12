# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the app and install Flask
COPY app.py .
RUN pip install flask

# Run the app
CMD ["python", "app.py"]