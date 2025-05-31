# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Copy the rest of the application code
COPY . .

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Build frontend assets
RUN if [ -f package.json ]; then npm install && npm run build || true; fi

# Expose port (customize if your app runs on a different port)
EXPOSE 8080

# Default command
# If using Flask:
# CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
# If using Gunicorn:
# CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
# If using another framework, adjust as needed.

CMD ["python", "app.py"]
