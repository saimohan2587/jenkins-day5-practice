#!/usr/bin/env python3
from netmiko import ConnectHandler

devices = [
    {"host": "10.10.10.2", "device_type": "cisco_ios", "username": "admin", "password": "admin"},
    {"host": "10.10.20.2", "device_type": "cisco_ios", "username": "admin", "password": "admin"}
]

# Save output directly to an artifact report file
with open("device_health_report.txt", "w") as report:
    for dev in devices:
        report.write(f"\n=== Device: {dev['host']} ===\n")
        ssh = ConnectHandler(**dev)
        output = ssh.send_command("show ip int br")
        report.write(output + "\n")
        print(f"=== Device: {dev['host']} ===\n{output}")
        ssh.disconnect()

print("\n[SUCCESS] device_health_report.txt generated!")
