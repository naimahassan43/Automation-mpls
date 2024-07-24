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

#find prompt to know mode
prompt = connection.find_prompt()
if '>' in prompt:
    connection.enable()   #entering User exec mode to Privileged mode

output = connection.send_command('sh ip int br')
print(output)

if not connection.check_config_mode():
    connection.config_mode()    #entering Privileged mode to Global configuration mode

print(connection.check_config_mode())

connection.send_command('username admin1 secret cisco')

print('Closing connection')
connection.disconnect()