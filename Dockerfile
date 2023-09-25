# Use the official Python image as the base image
FROM python:3.10-slim

# Create a working directory for your bot
WORKDIR /app

# Copy your bot's code and requirements.txt to the container
COPY . /app

# Install any dependencies using pip
# RUN pip install --no-cache-dir -r requirements.txt

# Set the bot token as an environment variable
CMD ["sh", "-c", "python your_bot_main_file.py $(cat config.json | jq -r '.token')"]
