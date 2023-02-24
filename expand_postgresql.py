import os

print('Configure tzdata')
os.system("dpkg-reconfigure locales >> log.txt 2>&1")
os.system("apt-get install tzdata -y >> log.txt 2>&1")

print('Expanding Postgresql')
os.system("apt-get install postgresql -y >> log.txt 2>&1")
os.system("service postgresql start >> log.txt 2>&1")

print("Creating db's myapp, myauth and user developer")
os.system("echo 'createdb myapp;' | sudo -i -u postgres >> log.txt 2>&1")
os.system("echo 'createdb myauth;' | sudo -i -u postgres >> log.txt 2>&1")
os.system("echo 'createuser developer;' | sudo -i -u postgres >> log.txt 2>&1")
os.system(f"echo 'postgres:postgres' | chpasswd")

