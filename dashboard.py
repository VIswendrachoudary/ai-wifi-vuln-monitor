import streamlit as st
import pandas as pd
from scapy.all import rdpcap, Dot11
import joblib

# Load model and packets
model = joblib.load("wifi_model.pkl")
packets = rdpcap("wifi_capture.pcap")

# Classify function
def classify_packet(pkt):
    if pkt.haslayer(Dot11):
        enc = 0 if pkt.FCfield & 0x40 else 1
        prediction = model.predict([[enc]])[0]
        return "Weak" if prediction == 0 else "Strong"
    return "Unknown"

# Run classification
results = [classify_packet(pkt) for pkt in packets if pkt.haslayer(Dot11)]

# Streamlit UI
st.title("📡 Wi-Fi AI Vulnerability Monitor")
st.markdown("Monitors captured Wi-Fi packets and flags weak encryption")

st.metric("🔢 Total Packets", len(results))
st.metric("🟥 Weak Encryption", results.count("Weak"))
st.metric("🟩 Strong Encryption", results.count("Strong"))

# Bar chart
st.subheader("Encryption Type Distribution")
st.bar_chart(pd.Series(results).value_counts())
