#!/usr/bin/env python3

"""
kcm = kill cmus
"""

import io
import os
from contextlib import redirect_stdout

# stackoverflow.com/a/40417352/6813490
stdout = io.StringIO()
with redirect_stdout(stdout):
	os.system('ps')
output = stdout.getvalue()

print(output)
