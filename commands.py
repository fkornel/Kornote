# pyright: reportMissingImports=false

import uuid
import sublime_plugin

class KornoteNewNoteCommand(sublime_plugin.WindowCommand):
	def run(self):
		print("Kornote: new note command triggered")
		self.window.status_message("Kornote: new note command triggered")

		note_id = str(uuid.uuid4())
		view = self.window.new_file()
		view.settings().set("kornote_id", note_id)
		view.set_name("Untitled Note")
		view.set_syntax_file("Packages/Text/Plain text.tmLanguage")
		view.set_scratch(True)