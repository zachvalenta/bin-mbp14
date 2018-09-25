#!/usr/bin/env python3

"""
qing = alternative to rm

send2trash version: 1.5.0
"""

import sys
from send2trash import send2trash

for i in sys.argv[1:]:
	try:
		send2trash(i)
	except OSError:
		print('❓  could not find file/dir to delete')
