import getpass
import telnetlib

HOST = input('enter the host ip address: ')
user = input("Enter your remote account: ")
password = getpass.getpass()
cmd = input('enter the only show command cmd: ')

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + b"\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + b"\n")
#Removed enable as user is configured with privllage level 15
#tn.write("enable\n")
#tn.write("Cisco\n")
tn.write(cmd + '\n')
tn.write('exit\n')

print tn.read_all()
