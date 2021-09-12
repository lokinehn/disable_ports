from netmiko import ConnectHandler


def connect(ip, user, passw, vendor):
    print('start connect')
    if vendor == 'Juniper':
        vendor_type = 'juniper_junos'
    elif vendor == 'Eltex':
        vendor_type = 'eltex'
    ssh = ConnectHandler(
            device_type=vendor_type,
            host=ip,
            username=user,
            password=passw
            )
    return ssh
