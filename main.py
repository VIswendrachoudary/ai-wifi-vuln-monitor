from scapy.all import rdpcap, Dot11
import joblib

# Load the trained model
model = joblib.load("wifi_model.pkl")

# Load the packet capture file
packets = rdpcap("wifi_capture.pcap")

def classify_packet(pkt):
    if pkt.haslayer(Dot11):
        # Simplified: assume WEP if "wep" found in raw packet
        enc = 0 if "wep" in str(pkt).lower() else 1
        prediction = model.predict([[enc]])[0]
        return "Weak" if prediction == 0 else "Strong"
    return "Unknown"

# Classify each packet
results = [classify_packet(pkt) for pkt in packets if pkt.haslayer(Dot11)]

# Print summary
print("=== Classification Summary ===")
print("Total Packets:", len(results))
print("Weak:", results.count("Weak"))
print("Strong:", results.count("Strong"))
