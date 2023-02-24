import os
from config import server_B
# server_B = '172.19.0.2'

print('Installing iptables')
os.system('apt-get install iptables -y  >> log.txt 2>&1')

print(f'Creating rules for {server_B}')
os.system(f'iptables -A INPUT -p tcp --dport 22 -s {server_B} -j DROP')

