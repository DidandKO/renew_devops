import os
from config import server_B

print('Installing Postgresql')
os.system("dpkg-reconfigure locales >> log.txt 2>&1")
os.system("apt-get install tzdata -y >> log.txt 2>&1")

os.system("apt-get install postgresql -y >> log.txt 2>&1")
os.system("usermod -aG sudo postgres")
os.system("service postgresql start >> log.txt 2>&1")

print('Checking connection')
os.system(f"echo 'developer' | psql -h {server_B} -U developer -d myapp")
