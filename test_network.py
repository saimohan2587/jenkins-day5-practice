import ipaddress
from push_network_configs import devices, commands

def test_device_ip_validity():
    """Verify all target devices have valid IPv4 addresses"""
    for dev in devices:
        assert ipaddress.IPv4Address(dev["host"])

def test_device_credentials_present():
    """Verify username and password are not blank"""
    for dev in devices:
        assert dev["username"] != ""
        assert dev["password"] != ""

def test_commands_list_not_empty():
    """Verify commands list has configurations to push"""
    assert len(commands) > 0
