from scapy.all import wrpcap, RadioTap, Dot11

# WEP flag in FCfield is bit 6 → value = 0x40
WEP_FLAG = 0x40

# Create 2 test packets: one WEP-like, one normal
packets = [
    RadioTap()/Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2="aa:bb:cc:dd:ee:ff", FCfield=WEP_FLAG),
    RadioTap()/Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2="11:22:33:44:55:66")
]

# Save to pcap file
wrpcap("wifi_capture.pcap", packets)
print("wifi_capture.pcap created successfully!")
