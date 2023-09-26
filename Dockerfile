FROM python:3.10-slim

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

# Set the bot token as an environment variable
ENV BOT_TOKEN="MTA4NTQ4NDA2Nzc5OTE3OTI4NA.GCEYDr.IdRxvFJYZCW4P5fBudtgTBj5RnVvGxCYfu_MIg"

# Run the bot
CMD python main.py