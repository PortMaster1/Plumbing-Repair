# Plumbing Repair

This is a repository for a raspberry pi to fix a problem at our church camp with people stealing WiFi.

Note: To run, run `sudo python3 main.py`

To set up MySQL server, run `sudo mysql_secure_installation` after `install.sh` is ran

# Installation

1. Install dependencies


to config db:
run `sudo mysql -u root -p`
Mow inside of MySQL prompt:
`-- Create database
CREATE DATABASE radius;

-- Create FreeRADIUS user
CREATE USER 'radius'@'localhost' IDENTIFIED BY 'radiuspass';

-- Grant permissions
GRANT ALL PRIVILEGES ON radius.* TO 'radius'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;
EXIT;`