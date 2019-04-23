#!/usr/bin/python3

print()

import sys


print("This is just a test.")
print()

if len(sys.argv) > 1:
  print("There was at least one argument.")
  for i in range(1, len(sys.argv)):
    print("  arg["+str(i)+"]: ", sys.argv[i])


print()


