#!/bin/bash
sudo apt update && sudo apt upgrade -y
sudo apt install freeradius -y

sudo apt install apache2 php php-mysql mariadb-server -y
sudo mysql_secure_installation
# Then configure database and install daloRADIUS from GitHub

sudo systemctl enable freeradius
sudo systemctl start freeradius

# Setup the AP as a client:

# Prompt for info
read -p "Enter Access Point IP address: " ip
read -p "Enter shared secret: " secret
read -p "Enter shortname: " shortname

# Append to the FreeRADIUS clients.conf file
cat <<EOF | sudo tee -a /etc/freeradius/3.0/clients.conf > /dev/null

client $shortname {
    ipaddr = $ip
    secret = $secret
    shortname = $shortname
}
EOF

echo "AP added as RADIUS client!"
sudo systemctl restart freeradius
echo "FreeRADIUS restarted."
echo "You do not need to run this script again, as it was stricly for install and setup of the FreeRADIUS client."