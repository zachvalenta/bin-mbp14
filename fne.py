#!/usr/bin/env python3
import os, argparse

def print_names(names, msg):
	print("{:*^30s}".format(msg))
	for name in names:
		print(name)
	print("\n")

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--start", help="starting index for file name slice", type=int, nargs='?', default=None)
parser.add_argument("-e", "--end", help="ending index for file name slice", type=int, nargs='?', default=None)
args = parser.parse_args()

orig_names = [x for x in os.listdir('.') if x[-3:]=="mp3" and os.path.isfile(x)]
print_names(orig_names, "original names")

if(args.end):
	args.end = -args.end
	new_names = [x[args.start:args.end-4]+".mp3" for x in os.listdir('.') if x[-3:]=="mp3" and os.path.isfile(x)]
else:
	new_names = [x[args.start:]+".mp3" for x in os.listdir('.') if x[-3:]=="mp3" and os.path.isfile(x)]

print_names(new_names, "updated names")

user_confirmation = input("look good? ('y' for yes, 'n' for no) ➡️   ")
if(user_confirmation=='y'):
	print('modification confirmed')
	for orig, new in zip(orig_names, new_names):
		os.rename(orig, new)
	print('🔼  modification complete')
else:
	print('🔽  modification aborted')

"""
TODOs:
how do `nargs` really work? -> https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
`default` perhaps unnecessary (bc if not passed arg defaults to None anyway)
fix `+".mp3"` hack (regex? https://pyformat.info/? )
colored text -> https://pypi.org/project/colorama/
"""

