"""
Check for installed packages
fyi, pip will install dependences
"""

import pip
import argparse

parser = argparse.ArgumentParser(description='Print list of installed packages')

parser.add_argument('--find', nargs='+', metavar='PKG', help="check if specific PKG or PKGs are installed, PKG can be a string or list", action='store')

args = parser.parse_args()

installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["{:}({:})".format(str.lower(i.key), i.version)
     for i in installed_packages])

if type(args.find) == list:
	chk = []
	for pkg in args.find:
		currchk = [s for s in installed_packages_list if str.lower(pkg) in s]
		if len(currchk) > 0:
			chk.extend(currchk)
		else:
			chk.append(pkg+' not found')
	[print(s) for s in chk]

elif type(args.find) == str:
	chk = [s for s in installed_packages_list if str.lower(args.find) in s]
	if not chk:
		print('Unable to find installed package',args.find)
	else:
		[print(s) for s in chk]

else:
	[print(s) for s in installed_packages_list]
	print('Total installed:',len(installed_packages_list))
