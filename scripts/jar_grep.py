#!//usr/bin/python3

"""
Very basic tool for searching through all the .jar files for interesting data,
without e.g. decompiling everything.
"""

JAR_PATH = "/usr/share/maltego"

import zipfile
import glob
import sys

if len(sys.argv) != 2:
	print("USAGE: python3 {} <search string>".format(sys.argv[0]))
	print(__doc__)
	exit()

for filename in glob.iglob(JAR_PATH + "/**/*.jar", recursive=True):
	jar = zipfile.ZipFile(filename)
	for subfile in jar.namelist():
		f = jar.open(subfile, "r")
		data = f.read()
		f.close()
		if sys.argv[1].encode() in data:
			print("{}:\t{}".format(filename, subfile))
