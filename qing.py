#!/usr/bin/env python3

"""
qing = alternative to rm

send2trash version: 1.5.0
"""

import sys
from send2trash import send2trash

for i in sys.argv[1:]:
	send2trash(i)
