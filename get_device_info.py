#!/usr/bin/env python3
from netmiko import ConnectHandler

# GNS3 Devices: Gateway R1 & Staging Switch
devices = [
    {"host": "10.10.10.2", "device_type": "cisco_ios", "username": "admin", "password": "admin"},
    {"host": "10.10.20.2", "device_type": "cisco_ios", "username": "admin", "password": "admin"}
]

for dev in devices:
    print(f"\n=== Device: {dev['host']} ===")
    ssh = ConnectHandler(**dev)
    print(ssh.send_command("show ip int br"))
    ssh.disconnect()
