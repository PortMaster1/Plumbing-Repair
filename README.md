# Plumbing Repair

This is a repository for a raspberry pi to fix a problem at our church camp with people stealing WiFi.

Note: To run, run `sudo python3 main.py`

To set up MySQL server, run `sudo mysql_secure_installation` after `install.sh` is ran

# Installation

1. Install dependencies


to config db:
run `sudo mysql -u root -p`
Mow inside of MySQL prompt:
```sql
-- Create database
CREATE DATABASE radius;

-- Create FreeRADIUS user
CREATE USER 'radius'@'localhost' IDENTIFIED BY 'radiuspass';

-- Grant permissions
GRANT ALL PRIVILEGES ON radius.* TO 'radius'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;
EXIT;
```
Now run `sudo mysql -u root -p radius < /etc/freeradius/3.0/mods-config/sql/main/mysql/schema.sql` to import FreeRADIUS schema
Now enable the sql module: `sudo ln -s /etc/freeradius/3.0/mods-available/sql /etc/freeradius/3.0/mods-enabled/`
Edit SQL config: `sudo nano /etc/freeradius/3.0/mods-available/sql`
Change:
```tezt
driver = "rlm_sql_mysql"
server = "localhost"
port = 3306
login = "radius"
password = "radiuspass"
radius_db = "radius"
```
Save and exit nano
Edit sites-enabled/default: `sudo nano /etc/freeradius/3.0/sites-enabled/default`
In these blocks, add sql (if it’s not already there):
	•	authorize {
	•	accounting {
	•	session {
	•	post-auth {
Example:
```text
authorize {
    ...
    sql
}

accounting {
    ...
    sql
}
```
Run `sudo systemctl restart freeradius` to restart FreeRADIUS