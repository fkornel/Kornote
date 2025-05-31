# pyright: reportMissingImports=false
# pyright: reportUnusedImport=false

import sublime
import sublime_plugin

class KornoteNewNoteCommand(sublime_plugin.WindowCommand):
	def run(self):
		print("Kornote: new note command triggered")
		self.window.status_message("Kornote: new note command triggered")

		note_view = self.window.new_file()
		note_view.set_name("Kornote Note")
		note_view.set_scratch(True)