# Base image
FROM python:3.10

# Working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the app using gunicorn (production-ready)
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
