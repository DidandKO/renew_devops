import os

user_name = "devops"

os.system("mkdir .ssh")
os.system(f"chown {user_name}:root /home/{user_name}/.ssh")
os.system("exit")

