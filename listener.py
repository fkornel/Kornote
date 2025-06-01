import sublime
import sublime_plugin
from .db import save_note

class KornoteEventListener(sublime_plugin.EventListener):
	def on_deactivated(self, view):
		note_id = view.settings().get("kornote_id")
		if not note_id:
			return

		content = view.substr(sublime.Region(0, view.size()))
		if not content.strip():
			return

		title = content.splitlines()[0]
		view.set_name(title)
		save_note(note_id, title, content)