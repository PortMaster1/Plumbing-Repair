#!/bin/bash
sudo python3 userlist_generator.py
echo "Successfully gwnerated userlist for FreeRADIUS"

sudo systemctl restart freeradius
echo "Restarting FreeRADIUS"