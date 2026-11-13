#!/usr/bin/env python3
"""
Push 3 minimal protocols (CDP, NTP, OSPF) safely to GNS3 devices.
Preserves all existing IP addresses and static routes.
"""
from netmiko import ConnectHandler

devices = [
    {"host": "10.10.10.2", "device_type": "cisco_ios", "username": "admin", "password": "admin"},
    {"host": "10.10.20.2", "device_type": "cisco_ios", "username": "admin", "password": "admin"}
]

# 3 Safe, Non-Destructive Protocols
commands = [
    "cdp run",                              # Protocol 1: Discovery (CDP)
    "ntp server 10.10.10.1",                # Protocol 2: Time Sync (NTP)
    "router ospf 1",                        # Protocol 3: Dynamic Routing (OSPF)
    "network 10.10.20.0 0.0.0.255 area 0"
]

for dev in devices:
    print(f"\n>>> Applying configurations to {dev['host']}...")
    ssh = ConnectHandler(**dev)
    output = ssh.send_config_set(commands)
    print(output)
    ssh.disconnect()

print("\n[SUCCESS] Configurations pushed safely!")
# SCM Test: Pushing new network change Fri Nov 13 15:27:03 IST 2026
