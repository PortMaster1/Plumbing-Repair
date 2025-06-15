import threading

from server import app
from sql_conmector import sql_thread

if __name__ == "__main__":
    db_thread = threading.Thread(target=sql_thread, daemon=True)
    db_thread.start()
    
    app.run(debug=True)