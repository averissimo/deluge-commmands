#!/usr/bin/python
import json
import sys, getopt, datetime
from StringIO import StringIO

def usage():
	print 'usage: '
	print '\t' + 'python deluge-json.py' + ' --torrentname <name> --log_path <path>'


def main(argv):
	try:
		opts, args = getopt.getopt(argv,"h",["torrentid=","torrentname=","torrentpath=","log_path=","no-write"])
   	except getopt.GetoptError as err:
		usage()
		sys.exit(2)
	args_len = 0
	no_write = 0
	for opt, arg in opts:
		if opt == '-h':
			usage()
			sys.exit()
		elif opt in ("--torrentid"):
			torrentid = arg
		elif opt in ("--torrentname"):
			torrentname = arg
			args_len += 1
		elif opt in ("--torrentpath"):
			torrentpath = arg
		elif opt in ("--log_path"):
			log_path = arg
			args_len += 1
		elif opt in ("--no-write"):
			no_write = 1
			args_len += 1
	if args_len < 2:
		usage()
		sys.exit()
	print str(log_path)

	new_completed = {"torrent": [{"timestamp": datetime.datetime.now().strftime("%c") ,"name": torrentname}]}

	try:
		json_data = open(log_path)
		data = json.load(json_data)
		data["completed"].append( new_completed )
		json_data.close()
	except KeyError:
		data["completed"] = new_completed
	except (IOError, ValueError):
		data = {}
		data["completed"] = new_completed

	if not no_write:
		json_data = open(log_path,"wb")
		json_data.write(json.dumps(data))
		json_data.close()
	else:
		print json.dumps(data, sort_keys=True,indent=2, separators=(',', ': '))
	

if __name__ == "__main__":
	main(sys.argv[1:])
