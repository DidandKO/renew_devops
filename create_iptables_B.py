import os
from config import server_C
#server_C = '172.19.0.3'

print('Installing iptables')
os.system('apt-get install iptables -y  >> log.txt 2>&1')

print(f'Creating rules for {server_C}')
os.system(f'iptables -A INPUT -p tcp --dport 22 -s {server_C} -j DROP')

