#!/usr/bin/python3

print()

import sys


print("This is just a test.")
print()

fc_name = None
config_id = None
using_lib = False

############################################
if len(sys.argv) > 1:
  print("There was at least one argument.")
  for i in range(1, len(sys.argv)):
    print("  arg["+str(i)+"]: ", sys.argv[i])
  #
  if sys.argv[1] == '--config':
    fc_name = sys.argv[2]
  elif sys.argv[1] == '--lib':
    using_lib = True
    from prs/sandy_lib import sandy_lib_print as sl_print
############################################


if using_lib:
  sl_print("Testing lib.")


############################################
if fc_name != None:
  f = open(fc_name)
  for l in f:
    if not l.startswith('!'):  continue
    l = l.strip()
    ll = l.split(' ')
    key = ll[0]
    #
    if key == '!config_id':
      config_id = ll[1]
  f.close()
############################################


if config_id != None:
  print("Found config.")
  print("  config_id: ", config_id)



print()


