#!/bin/bash

# Clear the terminal
clear

# Banner
echo -e "\033[92m"
echo "  ________        __         ____  __.__                "
echo " /  _____/  _____/  |_  ____ |    |/ _|  |   ___________ "
echo "/   \\  ___ /  _ \\   __\\/ __ \\|      < |  |_ / __ \\_  __ \\"
echo "\\    \\_\\  (  <_> )  | \\  ___/|    |  \\|  |_\\  ___/|  | \\/"
echo " \\______  /\\____/|__|  \\___  >____|__ \\____/\\___  >__|   "
echo "        \\/                 \\/        \\/         \\/       "
echo -e "\033[0m"

echo -e "\033[93mInstalling all required packages... Please wait.\033[0m"

# Read packages from requirements.txt and install them
while IFS= read -r package; do
    echo -e "\033[94mInstalling: $package\033[0m"
    pkg install -y $package
done < requirements.txt

# Install JADX
echo -e "\033[93mDownloading JADX...\033[0m"
wget https://github.com/skylot/jadx/releases/download/v1.4.7/jadx-1.4.7.zip

echo -e "\033[93mExtracting JADX...\033[0m"
unzip jadx-1.4.7.zip -d jadx
cd jadx/bin
chmod +x jadx
cd ../../

# Install Python libraries
echo -e "\033[93mInstalling Python libraries...\033[0m"
pip install tqdm

# Finish
echo -e "\033[92mAll dependencies installed successfully! You can now run the tool.\033[0m"
