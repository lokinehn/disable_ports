#Vendor's specific commands to disable ports

class Juniper:
    def __init__(self, connect):
        self.connect = connect
    def disablePort(self):
        self.ports = input('Enter port or ports (format 0/0/1 separator:","): ').split(',')
        for port in self.ports:
            command_disable = ['set interfaces ge-{} disable'.format(port.strip()),
                                'set interfaces ge-{}.0 disable'.format(port.strip())]
            self.connect.send_config_set(command_disable, exit_config_mode=False)
        self.connect.commit()
        self.connect.exit_config_mode()
        self.connect.disconnect()


class Eltex:
    def __init__(self, connect):
        self.connect = connect
    def disablePort(self):
        self.ports = input('Enter port or ports (format 1/0/1 separator:","): ')
        for port in self.ports:
            command_disable = ['interface gi{}'.format(port.strip()),
                                'shutdown',
                                'no port security']
            self.connect.send_config_set(command_disable)
        self.connect.disconnect()
