# 1. Use an official lightweight Python image
FROM python:3.11-slim

# 2. Set your working directory inside the container
WORKDIR /app

# 3. Copy only requirements first (caching layer)
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your application code
COPY . .

# 6. Expose the port your Flask app listens on
EXPOSE 5000

# 7. Define the command to run your app
CMD ["python", "app.py"]