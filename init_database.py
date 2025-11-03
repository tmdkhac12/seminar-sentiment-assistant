import sqlite3

# Kết nối hoặc tạo mới DB
conn = sqlite3.connect("sentiments.db")
cursor = conn.cursor()

# Tạo bảng (nếu chưa có)
cursor.execute("""
CREATE TABLE IF NOT EXISTS sentiments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    sentiment TEXT NOT NULL,
    timestamp DATETIME DEFAULT (datetime('now', '+7 hours'))
)
""")

conn.commit()
conn.close()
