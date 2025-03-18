#!/usr/bin/env python
"""
convert dos linefeeds (crlf) to unix (lf)
usage: python dos2unix.py
"""
import sys

original = sys.argv[1]
destination = sys.argv[2]

content = ''
outsize = 0

with open(original, 'rb') as infile:
    print("reading from:", original)
    content = infile.read()

with open(destination, 'wb') as output:
    print("writing to:", destination)
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))

print("Done. Saved %s bytes." % (len(content) - outsize))
