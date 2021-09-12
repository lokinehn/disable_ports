from getpass import getpass
from config import netmiko_connect
from config import netmiko_disable_ports
from config import netmiko_vendor_check

ip = input('Enter IP host: ')
vendor = netmiko_vendor_check.vendorCheck(ip)
print('Host is {}'.format(vendor))

user = input('Enter username to connect: ')
passw = getpass('Enter pass: ')

ssh = netmiko_connect.connect(ip, user, passw, vendor)

if vendor == 'Juniper':
    instance = netmiko_disable_ports.Juniper(ssh)
    instance.disablePort()
elif vendor == 'Eltex':
    instance = netmiko_disable_ports.Eltex(ssh)
    instance.disablePort()
