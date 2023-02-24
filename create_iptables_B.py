import os

os.system('apt-get install iptables -y')
os.system('iptables -A INPUT -p tcp --dport 22 -s 172.18.0.3 -j DROP')

