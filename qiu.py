#!/usr/bin/env python3

"""
qiu = wrapper around httpie

httpie version: 0.9.9
"""

import os
import sys

base = 'http://127.0.0.1:{}/{}'.format(sys.argv[1], sys.argv[2])
os.system('http {}'.format(base))
