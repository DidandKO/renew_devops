import os

os.system('''echo "create table test_auth (test_id int); REVOKE ALL ON ALL TABLES IN SCHEMA public FROM developer; GRANT SELECT, UPDATE ON ALL TABLES IN SCHEMA public TO developer;" | psql''')

