import mysql.connector
from userlist_generator import Generate, Reissue
from time import sleep

g = Generate()
r = Reissue()

_new_accounts = {}

@property
def new_accounts():
    return _new_accounts

@new_accounts.setter
def new_accounts(value):
    _new_accounts = {}
    _new_accounts = value

def sql_connector():
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
            return user
        else:
            return None
    
    # Clean up
    cursor.close()
    conn.close()

def sql_thread():
    while True:
        user = sql_connector()
        if user:
            r.find_user(user)
            ppsk = r.replace_ppsk(user)
            acct = {"name": user, "ppsk": ppsk}
            print(f'User "{user}" now has ppsk "{ppsk}"'
            new_accounts[user] = ppsk
        sleep(60) # Sleeps for 1 minute before checking again.