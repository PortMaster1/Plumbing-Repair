#!/bin/bash
sudo apt update && sudo apt upgrade -y
sudo apt install freeradius -y

sudo apt install apache2 php php-mysql mariadb-server -y
sudo mysql_secure_installation
# Then configure database and install daloRADIUS from GitHub

sudo systemctl enable freeradius
sudo systemctl start freeradius

chmod +x update_clients.sh

echo "You do not need to run this script again, as it was stricly for install and setup of the FreeRADIUS client."