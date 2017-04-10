from paramiko.client import *
import paramiko
from funcs.funcs import *

# host = '10.100.0.84'
# user = 'root'
# password = '4linux'
#
# client = SSHClient()
#
# client.load_system_host_keys()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# client.connect(hostname=host, username=user, password=password)
# stdin, stdout, stderr = client.exec_command("ls -la")
#
# print stdout.read()

    #------- DATETIME
# Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.
from datetime import datetime, timedelta
# PEGA O ANO DA DATA ATUAL
print datetime.now()
print datetime.today()
print datetime.now() + timedelta(4)
print datetime(1990, 8, 1, 0, 0, 0)

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(hostname=host, username=user, password=password)
stdin, stdout, stderr = client.exec_command("psql")

print stdout.read()

    #------- DATETIME
# Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.
import datetime
# PEGA O ANO DA DATA ATUAL
a = datetime.datetime.today().year
