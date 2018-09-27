#!/usr/bin/env python3

"""
qiu = wrapper around httpie

httpie version: 0.9.9
"""

# TODO: handle HTTP verbs

import os
import sys


def make_url(port, path):
	url = 'http://127.0.0.1:{}/{}'.format(port, path)
	return url


port_num = sys.argv[1]

try:
	path_name = sys.argv[2]
except IndexError:
	path_name = ''

os.system('http {}'.format(make_url(port_num, path_name)))
