# Use a light version of Python
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all your files into the container
COPY . .

# Install the libraries from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Tell Docker the app runs on port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]