import sqlite3
import os
import sublime

DB_PATH = os.path.join(sublime.packages_path(), "Kornote", "kornote.db")

def init_db():
	print("Kornote: initializing DB")
	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	c.execute("""
		CREATE TABLE IF NOT EXISTS notes (
			id TEXT PRIMARY KEY,
			title TEXT,
			content TEXT,
			created_at TEXT,
			updated_at TEXT
		)
	""")
	conn.commit()
	conn.close()
	print("Kornote: DB has been created")