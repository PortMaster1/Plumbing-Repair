#!/bin/bash
sudo python3 userlist_generator.py
echo "Successfully gwnerated userlist for FreeRADIUS"

sudo rm -f /etc/freeradius/3.0/mods-config/files/authorize
sudo mv ./authorize /etc/freeradius/3.0/mods-config/files/authorize
echo "Successfully moved userlist to FreeRADIUS's folder."

sudo systemctl restart freeradius
echo "Restarting FreeRADIUS"