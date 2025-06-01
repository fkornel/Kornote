# pyright: reportMissingImports=false

import sqlite3
import os
import sublime
from datetime import datetime

DB_PATH = os.path.join(sublime.packages_path(), "Kornote", "kornote.db")

def init_db():
	print("Kornote: db.init_db")
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

def save_note(note_id, title, content):
	print("Kornote: db.save_note")
	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()

	now = datetime.utcnow().isoformat()
	c.execute("""
		INSERT INTO notes (id, title, content, created_at, updated_at)
		VALUES (?, ?, ?, ?, ?)
		ON CONFLICT(id) DO UPDATE SET
			title=excluded.title,
			content=excluded.content,
			updated_at=excluded.updated_at
	""", (note_id, title, content, now, now))

	conn.commit()
	conn.close()

