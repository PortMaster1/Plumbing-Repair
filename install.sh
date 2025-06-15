#!/bin/bash
sudo apt update && sudo apt upgrade -y
sudo apt install freeradius -y

sudo apt install apache2 php php-mysql mariadb-server -y
sudo mysql_secure_installation
# Then configure database and install daloRADIUS from GitHub

sudo ln -s /etc/freeradius/3.0/mods-available/sql /etc/freeradius/3.0/mods-enabled/
# Configure DB in /etc/freeradius/3.0/mods-enabled/sql
# (use mysql, provide username/password)

mysql -u root -p radius < /etc/freeradius/3.0/mods-config/sql/main/mysql/schema.sql

# Enable SQL in sites-enabled/default
# Under accounting { and authorize {, add:
# sql

sudo systemctl enable freeradius
sudo systemctl start freeradius

chmod +x update_clients.sh

pip install mysql-connector-python --break-system-packages

echo "You do not need to run this script again, as it was stricly for install and setup of the FreeRADIUS client."