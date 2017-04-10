from paramiko.client import SSHClient
import paramiko
import os

client = SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host = '10.100.0.84'
user = 'root'
password = '4linux'

client.connect(hostname=host, username=user, password=password)
stdin, stdout, stderr = client.exec_command("ls la")

if stderr.channel.recv_exit_status() != 0:
    print stderr.channel.recv_exit_status()
    print stderr.read()
else:
    print stdout.read()




# print os.popen("ls -la").read()
