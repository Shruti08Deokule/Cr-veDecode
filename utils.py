# utils.py

import sqlite3
from datetime import date, timedelta

def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entry_date TEXT,
            craving TEXT,
            hunger_type TEXT,
            mood TEXT,
            water REAL
        )
    ''')
    conn.commit()
    conn.close()

def insert_log(entry_date, craving, hunger_type, mood, water):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO logs (entry_date, craving, hunger_type, mood, water) VALUES (?, ?, ?, ?, ?)",
              (entry_date, craving, hunger_type, mood, water))
    conn.commit()
    conn.close()

def fetch_weekly_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    last_week = date.today() - timedelta(days=7)
    c.execute("SELECT craving, COUNT(*) FROM logs WHERE entry_date >= ? GROUP BY craving", (last_week.isoformat(),))
    data = c.fetchall()
    conn.close()
    return data

def fetch_summary_stats():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    last_week = date.today() - timedelta(days=7)
    c.execute("SELECT AVG(water), COUNT(*), SUM(mood = '😊 Happy') FROM logs WHERE entry_date >= ?", (last_week.isoformat(),))
    result = c.fetchone()
    conn.close()
    return result
