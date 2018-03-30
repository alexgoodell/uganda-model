import os
import sys

sys.dont_write_bytecode = True

# ---------------- Configuration --------------


# find root path
current_path = os.getcwd()
root_path = current_path.split('uganda-model', 1)[0] + 'uganda-model'


data_path = root_path + "/data"
notebook_path = root_path + "/notebooks"
lib_path = root_path + "/lib"
refs_path = root_path + "/refs"
tmp_path = root_path + "/tmp"


# required to use as module
if __name__ == '__main__': 
	print "hello world"