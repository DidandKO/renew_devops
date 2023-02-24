import os 
import subprocess
import time
import json

def ok_output(function):
	def do_function(*args, **kwargs):
		print('_' * 10)
		time_start = time.time()
		function(*args, **kwargs)
		time_end = round(time.time() - time_start, 2)
		print(f'	{function.__name__}: time - {time_end}')
	return do_function
		

class Renew:
	def __init__(self):
		self.server_B = None
		self.server_C = None
		self.create_docker_image("ubuntu-ssh:latest")
		self.expand_server(2)
		os.system("ssh-keygen")
		
	
	def get_server_ip(self):
		b = os.popen('docker container inspect renew_server_1').read()
		self.server_B = json.loads(b)[0]["NetworkSettings"]["Networks"]['renew_default']['IPAddress']
		c = os.popen('docker container inspect renew_server_2').read()
		self.server_C = json.loads(c)[0]["NetworkSettings"]["Networks"]['renew_default']['IPAddress']
		return True
		
	
	def create_docker_image(self, image_name):
		print(f"Creating image {image_name}")
		os.system(f"docker build . -t {image_name} >> log.txt 2>&1")
	
	@ok_output
	def expand_server(self, server_count):
		print(f"Expanding {server_count} servers")
		os.system(f'docker-compose up -d --scale server={server_count}')
		# sudo docker exec -ti 9e68d752aeb1 /bin/bash
		self.get_server_ip()
		print(self.server_B)
		print(self.server_C)
		return True
	
	def connect_to_server_and_do(self, server_ip, user_name, python_script):
		os.system(f"cat {python_script} | ssh {user_name}@{server_ip} 'cat > {python_script}; echo '{user_name}' | sudo -S python3 {python_script}' >> log.txt 2>&1")
	
	def connect_to_server_and_do_no_sudo(self, server_ip, user_name, python_script):
		os.system(f"cat {python_script} | ssh {user_name}@{server_ip} 'cat > {python_script}; python3 {python_script}' >> log.txt 2>&1")
		
	@ok_output
	def disable_SSH_auth_by_passwd(self, server_ip, user_name):
		print(f"Disabling SSH password auth from {server_ip}, under {user_name}")
		os.system(f"cat ~/.ssh/id_rsa.pub | ssh {user_name}@{server_ip} 'cat > ~/.ssh/authorized_keys'")
		return True
	
	@ok_output	
	def create_user(self, server_ip, user_name, user_to_create):
		print(f"Creating user {user_to_create} on {server_ip}")
		self.connect_to_server_and_do(server_ip, user_name, 'create_user.py')
		self.connect_to_server_and_do(server_ip, user_to_create, 'create_ssh_folder.py')
		self.disable_SSH_auth_by_passwd(server_ip, user_to_create)
		return True
	
	@ok_output	
	def expand_postgresql_ops(self, server_ip, user_name):
		print(f"Installing PostgreSQL on {server_ip} with user {user_name}")
		self.connect_to_server_and_do(server_ip, user_name, 'expand_postgresql.py')
		self.connect_to_server_and_do_no_sudo(server_ip, 'postgres', 'change_password.py')
		self.connect_to_server_and_do_no_sudo(server_ip, 'postgres', 'give_developer_rights_to_myapp.py')
		self.connect_to_server_and_do_no_sudo(server_ip, 'postgres', 'give_developer_rights_to_myauth.py')	
		return True
	
	@ok_output	
	def allow_postgresql_access(self, server_ip):
		print(f"Allowing access to postgresql for user developer from {server_ip}")
		self.connect_to_server_and_do_no_sudo(server_ip, 'postgres', 'access_from_C.py')
		return True
	
	@ok_output
	def check_postgresql_access(self, server_ip, user_name):
		print(f"Checking access from {server_ip} to developer")
		self.connect_to_server_and_do(server_ip, user_name, 'check_access.py')
		return True
	
	@ok_output	
	def init_firewall_rules(self):
		print(f"Initiating iptables rules")
		self.connect_to_server_and_do(self.server_B, 'test', 'create_iptables_B.py')
		self.connect_to_server_and_do(self.server_C, 'test', 'create_iptables_C.py')
		return True
	
	def do(self):
		self.disable_SSH_auth_by_passwd(self.server_B, 'test')
		self.create_user(self.server_B, 'test','devops')
		self.expand_postgresql_ops(self.server_B, 'test')
		self.allow_postgresql_access(self.server_B)
		self.check_postgresql_access(self.server_C, 'test')
		self.init_firewall_rules()

if __name__ == '__main__':
	rn = Renew()
	rn.do()

