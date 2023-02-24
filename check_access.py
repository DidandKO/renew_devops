import os

os.system("dpkg-reconfigure locales")
os.system("apt-get install tzdata -y")

os.system("apt-get install postgresql -y")
os.system("usermod -aG sudo postgres")
os.system("service postgresql start")
os.system("echo 'developer' | psql -h 172.18.0.2 -U developer -d myapp")
