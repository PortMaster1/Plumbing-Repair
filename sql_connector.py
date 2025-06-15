import mysql.connector

# Connect to your FreeRADIUS SQL DB
conn = mysql.connector.connect(
    host="localhost",
    user="radius",           # replace with your DB user
    password="your_password",# replace with your DB password
    database="radius"        # default FreeRADIUS DB name
)

cursor = conn.cursor()

# SQL query: active sessions only
cursor.execute("""
    SELECT username, callingstationid, acctstarttime
    FROM radacct
    WHERE acctstoptime IS NULL
""")

# Track number of devices per user
user_devices = {}

for username, mac, start_time in cursor.fetchall():
    user_devices.setdefault(username, set()).add(mac)

# Print users with more than 2 devices
for user, devices in user_devices.items():
    if len(devices) > 2:
        print(f"⚠️  User '{user}' has {len(devices)} active devices: {devices}")

# Clean up
cursor.close()
conn.close()