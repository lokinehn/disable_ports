import subprocess

#Check vendor of network device by sending default SNMP request
def vendorCheck(ip):
    snmpwalk_get = subprocess.run('snmpwalk -v2c -c public {} 1.3.6.1.2.1.1.1.0'.format(ip), shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).stdout.decode('utf-8')
    #Two examples
    if snmpwalk_get.find('MES') != -1:
        return 'Eltex'
    elif snmpwalk_get.find('Juniper') != -1:
        return 'Juniper'
