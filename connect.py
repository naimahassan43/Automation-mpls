from netmiko import Netmiko

connection = Netmiko(host = '192.168.150.111', port = '22' , username = 'admin', password = 'cisco', device_type='cisco_ios')
