#!/bin/bash

# Setup script for Raspberry Pi App

set -e  # error exit

echo "🚀 Starting setup for NutriFridge App..."

# Update system and install dependencies
echo "🔧 Installing system packages..."
sudo apt update && sudo apt install -y \
  python3-pip \
  python3-venv \
  libatlas-base-dev \
  libjpeg-dev \
  libtiff5 \
  libjasper-dev \
  libpng-dev \
  libavcodec-dev \
  libavformat-dev \
  libswscale-dev \
  libv4l-dev \
  libxvidcore-dev \
  libx264-dev \
  libfontconfig1 \
  libfreetype6 \
  libhdf5-dev \
  libharfbuzz0b \
  libfribidi0 \
  libxcb1 \
  python3-pyqt5

# setup virtual env
echo "🐍 Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# install reuirements
echo "📦 Installing Python packages from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

# finished
echo "✅ Setup complete. Virtual environment activated."
echo "👉 Run your app using: python main.py"
