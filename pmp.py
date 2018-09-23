#!/usr/bin/env python3

"""
pmp = Python make Python (project)
"""


import os
import sys


def make_dirs(dirs):
	for dir in dirs:
		os.makedirs(dir)


def make_files(files):
	for file in files:
		open(file, 'w').close()


def write_file(file, content):
	f = open(file, 'w')
	f.write(content)
	f.close()


# PACKAGES, MODULES, FILES
project_root = sys.argv[1]
pkgs = ['source', 'tests']
root_files = ['README.md']
source_mods = ['sut.py']
test_mods = ['__init__.py', 'test_sut.py']

# CODE
source_code = """def return_something():
	return "something"
"""

test_code = """import unittest


class TestSUT(unittest.TestCase):
	
	def test_sanity(self):
		self.assertEqual(True, True)
"""

# WRITE ROOT
make_dirs([project_root])
os.chdir(project_root)
make_dirs(pkgs)
make_files(root_files)

# WRITE SOURCE
os.chdir('source')
make_files(source_mods)
write_file('sut.py', source_code)

# WRITE TESTS
os.chdir('../tests')
make_files(test_mods)
write_file('test_sut.py', test_code)

# RUN TESTS
os.system('python3 -m unittest discover')

# GIT
os.chdir('..')
os.system('git init')
os.system('git add .')
os.system("git commit -m 'bootstrap project' ")
os.system('git log --graph -n 10 --oneline --all --decorate')
