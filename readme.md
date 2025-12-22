# CIPHER-CAMPHISH-PRO
> **Deciphering the future before it happens..**

CIPHER-CAMPHISH-PRO is an automated security framework designed for auditing browser vulnerabilities and client-side data leakage. It integrates high-fidelity social engineering templates with automated exfiltration modules to demonstrate the risks of unauthorized media and telemetry access.

## Release Information
* **Version:** 10.0.1-stable
* **Platform:** Linux / Termux
* **Network Protocol:** HTTPS / WebRTC / Telegram API

## Core Features
* **Media Auditing:** Automated webcam snapshot capture at configurable intervals.
* **System Telemetry:** Extraction of hardware identifiers (GPU, RAM, CPU cores).
* **Location Mapping:** HTML5-based latitude and longitude coordinate retrieval.
* **Network Reconnaissance:** Internal IP discovery bypassing VPNs via WebRTC STUN requests.
* **Persistence:** Tab-cloaking and background process management.

## Social Engineering Templates
The framework includes several pre-configured decoys:
1. **Security Audit:** System integrity and security diagnostic simulation.
2. **Virtual Meetings:** Pre-join hardware calibration for Zoom and MS Teams.
3. **Media Sync:** Acoustic and visual interface testing for Spotify/Netflix.
4. **Crypto Verification:** Hardware wallet and security link validation.

## Deployment Guide

### Prerequisites
* Python 3.x
* PHP
* SSH Tunneling service (Cloudflared recommended for WAN)

### Installation
```bash
# Clone the repository
git clone [https://github.com/cipher-attack/camphish-pro.git](https://github.com/cipher-attack/camphish-pro.git)

# Navigate to project directory
cd camphish-pro

# Set execution permissions
chmod +x *

# Initialize the framework
./cipher.sh
```

### Usage Note
For local network testing, select **Localhost**. For remote auditing outside your local network, utilize the **Cloudflared** option to establish a secure tunnel.

---

## Author

<div align="left">
  <img src="https://github.com/cipher-attack.png" width="130" align="left" style="border-radius: 10px; margin-right: 20px; border: 2px solid #10b981;" />
  <h3>Biruk Getachew (CIPHER)</h3>
  <p><i>Offensive Security Researcher | AI Integrator</i></p>
  <p>I am a 12th-grade student focused on Offensive Security and Neural Systems. I specialize in mobile-centric development environments, specifically leveraging LLMs to automate vulnerability discovery and security reconnaissance workflows.</p>
  <p>
    <a href="https://github.com/cipher-attack">GitHub</a> • 
    <a href="https://www.youtube.com/@cipher-attack">YouTube</a> • 
    <a href="https://t.me/cipher_attacks">Telegram</a>
  </p>
</div>

<br clear="left"/>

---

## Disclaimer
This tool is for authorized security testing and educational purposes only. Unauthorized use is a violation of law. The developer assumes no responsibility for misuse of this software.
