# pyright: reportMissingImports=false
# pyright: reportUnusedImport=false

from .db import init_db

def plugin_loaded():
	init_db()


