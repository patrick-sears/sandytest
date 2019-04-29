#!/usr/bin/python3

print()

import sys
# from prs/sandy_print import sandylib_print as sl_print
# import prs.sandylib


print("This is just a test.")
print()

fc_name = None
config_id = None
using_lib = 0

############################################
if len(sys.argv) > 1:
  print("There was at least one argument.")
  for i in range(1, len(sys.argv)):
    print("  arg["+str(i)+"]: ", sys.argv[i])
  #
  if sys.argv[1] == '--config':
    fc_name = sys.argv[2]
  elif sys.argv[1] == '--local_lib':
    using_lib = 1
  elif sys.argv[1] == '--installed_lib':
    using_lib = 2
############################################


if using_lib == 1:
  from libs.sandylib import sandylib_print as sl_print
  sl_print("Testing lib.")
elif using_lib == 2:
  from prs.sandylib import sandylib_print as sl_print
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


