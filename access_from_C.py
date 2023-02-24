import os
from config import server_C

print('Adding configure info')
postgresql_conf = os.popen("psql -c 'SHOW config_file;'|grep postgresql").read()
os.system(f'''echo "listen_addresses = '*'" >> {postgresql_conf}''')
os.system(f"echo 'host    all             developer       {server_C}/32           password' >> {postgresql_conf.replace('postgresql.conf', 'pg_hba.conf')}")

print('Restarting postgresql service')
os.system(f"service postgresql restart")

