# Use base Linux image
FROM ubuntu:22.04

# Set environment non-interactive
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt update && apt install -y \
    python3 python3-pip aircrack-ng tcpdump \
    libpcap-dev git iproute2

# Install Python libs
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy your app
COPY . /app
WORKDIR /app

# Run your Python CLI
CMD ["python3", "monitor.py"]
