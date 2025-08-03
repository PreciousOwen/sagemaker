FROM nvidia/cuda:11.3.1-runtime-ubuntu20.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    git wget unzip build-essential \
    python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy Meshroom binaries
COPY meshroom_bin /opt/ml/code/meshroom_bin

# Copy pipeline script
COPY run_pipeline.py /opt/ml/code/run_pipeline.py

WORKDIR /opt/ml/code
ENTRYPOINT ["python3", "run_pipeline.py"]
