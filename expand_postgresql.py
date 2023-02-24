import os

user_name = "devops"
os.system("usermod -aG sudo postgres")

os.system("dpkg-reconfigure locales")
os.system("apt-get install tzdata -y")

os.system("apt-get install postgresql -y")
os.system("service postgresql start")
os.system("echo 'createdb myapp; createdb myauth; createuser developer;' | sudo -i -u postgres")
os.system(f"echo 'postgres:postgres' | chpasswd")

