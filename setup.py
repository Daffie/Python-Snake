import sys
from cx_Freeze import setup, Executable

build_exe_options = {"includes" : ["re"]}

base = None
if sys.platform == "win32":
	base = "Win32GUI"

setup(	name = "Python-Snake",
	version = "0.1",
	description = "Python-Snake, a Snake Game in Python",
	options = {"build_exe": build_exe_options},
	executables = [Executable("testmap.pyw", base = base)])