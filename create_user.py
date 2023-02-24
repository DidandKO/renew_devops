import os

user_name = 'devops'

os.system(f"useradd -rm -d /home/{user_name} -p {user_name} -s /bin/bash -g root -G sudo -u 1001 {user_name}") # passwd=devops
os.system(f"usermod -aG sudo {user_name}")
os.system(f"echo {user_name}:{user_name} | chpasswd")
os.system("echo 'devops ALL=(ALL:ALL) NOPASSWD:ALL' >> /etc/sudoers") # add 'devops ALL=(ALL:ALL) NOPASSWD:ALL'
os.system("exit")


