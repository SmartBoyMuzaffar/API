import os
import time

os.system("sudo chmod 700 -R /var/lib/postgresql/15/main")
os.system("/usr/lib/postgresql/15/bin/pg_ctl restart -D /var/lib/postgresql/15/main")
time.sleep(3)
os.system("systemctl restart api")
time.sleep(1)

# sudo systemctl status postgresql@15-main.service
# pg_lsclusters
# sudo chmod 700 -R /var/lib/postgresql/15/main
# sudo -i -u postgres
# /usr/lib/postgresql/15/bin/pg_ctl restart -D /var/lib/postgresql/15/main
# exit

