# 🛡️ AI Wi-Fi Vulnerability Monitor

An AI-powered tool to monitor and classify Wi-Fi packets based on potential security weaknesses.

## 🔍 Features

- 📡 Captures real-time Wi-Fi packets (via `airodump-ng` / `tcpdump`)
- 🧠 Classifies packets using Machine Learning (weak vs strong auth)
- 📊 Provides summary reports on packet security
- 🐍 Built using Python with Scapy and scikit-learn
- 🖥️ CLI-based interface with optional GUI visualization coming soon

## 🚀 How It Works

1. **Packet Capture**  
   Captures packets using external tools like `airodump-ng` or `tcpdump`.

2. **Parsing with Scapy**  
   Parses `.pcap` files and extracts features from each packet.

3. **AI Classification**  
   Uses a trained ML model to detect and label weak authentication attempts.

4. **Summary Output**  
   Outputs a summary of total packets analyzed and their classification.

## 🧪 Requirements

- Python 3.7+
- scapy
- scikit-learn
- pandas
- joblib
- matplotlib (optional for future GUI)
- aircrack-ng (for live capture)

## ⚙️ Installation

```bash
git clone https://github.com/VIswendrachoudary/ai-wifi-vuln-monitor.git
cd ai-wifi-vuln-monitor
pip install -r requirements.txt