import os

postgresql_conf = os.popen("psql -c 'SHOW config_file;'|grep postgresql").read()
os.system(f'''echo "listen_addresses = '*'" >> {postgresql_conf}''')
os.system(f"echo 'host    all             developer       172.18.0.3/32           password' >> {postgresql_conf.replace('postgresql.conf', 'pg_hba.conf')}")
os.system(f"service postgresql restart")

