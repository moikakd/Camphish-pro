#!/bin/bash
echo "[*] Installing CIPHER-X ELITE v10.0 Dependencies..."
pkg update && pkg upgrade -y
pkg install python php wget curl unzip -y
pip install -r requirements.txt
chmod +x cipher.sh core/*
echo "[+] Setup Complete. Run ./cipher.sh to start."