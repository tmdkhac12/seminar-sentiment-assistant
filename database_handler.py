import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "sentiments.db")

def save_sentiment_to_db(dictionary):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    text = dictionary["text"]
    sentiment = dictionary["sentiment"]

    cursor.execute("""
        INSERT INTO sentiments (text, sentiment)
        VALUES (?, ?)
    """, (text, sentiment))

    conn.commit()
    conn.close()

def get_all_sentiments():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM sentiments
        ORDER BY timestamp desc 
        LIMIT 50
    """)

    result = cursor.fetchall()

    return result