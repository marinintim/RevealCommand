import sublime
import sublime_plugin

class RevealCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.window().run_command("reveal_in_side_bar")

class RevealFinder(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.window().run_command("open_dir", {"dir": "$file_path", "file": "$file_name"})
