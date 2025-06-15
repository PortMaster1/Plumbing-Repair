#!/bin/bash
sudo apt update && sudo apt upgrade -y
sudo apt install freeradius -y

sudo apt install apache2 php php-mysql mariadb-server -y
# Then configure database and install daloRADIUS from GitHub



sudo systemctl enable freeradius
sudo systemctl start freeradius

chmod +x update_clients.sh

pip install mysql-connector-python --break-system-packages

# Install daloradius
cd /var/www/html
wget https://github.com/lirantal/daloradius/archive/1.3.zip
unzip 1.3.zip
mv daloradius-1.3 daloradius
sudo mysql -u root -p radius < daloradius/contrib/db/fr2-mysql-daloradius-and-freeradius.sql
sudo mysql -u root -p radius < daloradius/contrib/db/mysql-daloradius.sql
sudo cp daloradius/library/daloradius.conf.php.sample daloradius/library/daloradius.conf.php
# Edit DB credentials in config file
sudo chown -R www-data:www-data daloradius
sudo chmod 664 daloradius/library/daloradius.conf.php
sudo systemctl restart freeradius

echo "You do not need to run this script again, as it was stricly for install and setup of the FreeRADIUS client."