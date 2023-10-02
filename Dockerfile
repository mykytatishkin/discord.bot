FROM debian:buster-slim

# Create a working directory for your bot
WORKDIR /app

# Copy your bot's code, requirements.txt, and config.json to the container
COPY . /app

# Install any dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Install jq
RUN apt-get update && apt-get install -y jq

# Expose a TCP port
EXPOSE 8080

# Run the bot
CMD python main.py
