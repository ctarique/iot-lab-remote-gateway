# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies (only what we need)
RUN pip install Flask pyserial

# Copy your code into the container
COPY app.py .
COPY templates/ ./templates/

# Expose the Flask port
EXPOSE 5000

# Run the gateway
CMD ["python", "app.py"]
