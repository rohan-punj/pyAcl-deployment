from netmiko import ConnectHandler
from getpass import getpass
import time
import re
import ipaddress


user = input("Enter your SSH username: ")
PASS = getpass()

with open('ios_devices.txt') as routers:
    for IP in routers:
        Router = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'username': user,
            'password': PASS,
        }
        myssh = ConnectHandler(**Router)
        hostname = myssh.send_command('show run | i host')
        x = hostname.split()
        devicename = x[1]
        myssh.send_config_from_file('acl_mgmt.txt')
        myssh.send_config_from_file('acl_snmp.txt')
        print(devicename + ' Configured')
        output = myssh.send_command('show run | sec acl_mgmt')
        print(output)
        output = myssh.send_command('show run | sec acl_snmp')
        print(output)
        myssh.disconnect()

with open('nxos_devices.txt') as routers:
    for IP in routers:
        Router = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'username': user,
            'password': PASS,
        }
        myssh = ConnectHandler(**Router)
        hostname = myssh.send_command('show run | i host')
        x = hostname.split()
        devicename = x[1]
        myssh.send_config_from_file('nxos_acl_mgmt.txt')
        myssh.send_config_from_file('nxos_acl_snmp.txt')
        print(devicename + ' Configured')
        output = myssh.send_command('show run | sec acl_mgmt')
        print(output)
        output = myssh.send_command('show run | sec acl_snmp')
        print(output)
        myssh.disconnect()

input('Press ENTER To Continue')