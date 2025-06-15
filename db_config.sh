sudo mysql_secure_installation

sudo ln -s /etc/freeradius/3.0/mods-available/sql /etc/freeradius/3.0/mods-enabled/
# Configure DB in /etc/freeradius/3.0/mods-enabled/sql
# (use mysql, provide username/password)

mysql -u root -p radius < /etc/freeradius/3.0/mods-config/sql/main/mysql/schema.sql

# Enable SQL in sites-enabled/default
# Under accounting { and authorize {, add:
# sql