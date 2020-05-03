import getpass
import telnetlib

HOST = input('enter the host ip address: ')
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + b"\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + b"\n")

tn.write("enable\n")
tn.write("Cisco\n")
cmd = input('enter the only show command cmd: ')
tn.write(cmd + '\n')
tn.write('exit\n')

print tn.read_all()
