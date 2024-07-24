#from netmiko import Netmiko
#connection = Netmiko(host = '192.168.150.111', port = '22' , username = 'admin', password = 'cisco', device_type='cisco_ios')

from netmiko import ConnectHandler

cisco_device = {
    'device_type':'cisco_ios',
    'host' : '192.168.150.111', 
    'username' : 'admin', 
    'password' : 'cisco',
    'port': '22',
    'secret': 'cisco'
}

connection = ConnectHandler(**cisco_device)  
output = connection.send_command('sh ip int br')
print(output)


print('Closing connection')
connection.disconnect()