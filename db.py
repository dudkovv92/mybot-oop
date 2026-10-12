import sqlite3

class DB:
    def __init__(self, path):
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
        self.conn.commit()

    def set_name(self, user_id, name):
        self.cur.execute("INSERT OR REPLACE INTO users (id, name) VALUES (?, ?)", (user_id, name))
        self.conn.commit()

    def get_name(self, user_id):
        self.cur.execute("SELECT name FROM users WHERE id = ?", (user_id,))
        row = self.cur.fetchone()
        return row[0] if row else None