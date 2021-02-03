class print():
	def red(text):
		import sys
		sys.stderr.write(text)
		del sys
	def blue(text):
		import sys
		sys.stdout.write(text)
		del sys
	def normal(text):
		print(text)

class string():
	def rem(inp, wtr):
		return inp.replace(wtr, "")
	def remove(inp, wtr):
		return inp.replace(wtr, "")
	def delete(inp, wtr):
		return inp.replace(wtr, "")
	def test(self, wtr):
		return self.replace(wtr, "")

class int():
	def random(min, max):
		from random import randint
		ret = randint(min, max)
		del randint
		return ret
	def square(int):
		return int ** 2

class path():
	def desktop():
		import os
		return os.path.join("C:\\", os.environ["HOMEPATH"], "Desktop\\")
		del os
	def user():
		import os
		return os.path.join("C:\\", os.environ["HOMEPATH"]) + "\\"
		del os