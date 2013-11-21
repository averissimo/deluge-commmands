#!/usr/bin/python
import json
import sys, getopt, datetime
from StringIO import StringIO

def usage():
	print 'usage: '+ 'python deluge-json.py' + ' [--no-write ]--torrentname <name> --log_path <path>'
	print ''
	print 'options:'
	print '\t --no-write\n\t\tonly print result and do not write to file'
	print '\t --torrentname\n\t\tname of torrent'
	print '\t --log_path\n\t\tpath to log file'
	print ''
	print '\tnote: if name or path has spaces, then it should be surrounded by ""'

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"h",["torrentid=","torrentname=","torrentpath=","log_path=","no-write","element="])
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
		elif opt in ("--element"):
			element = arg
			args_len += 1
	if args_len < 3:
		usage()
		sys.exit()
	print str(log_path)

	new_completed = {"torrent": [{"timestamp": datetime.datetime.now().strftime("%c") ,"name": torrentname}]}

	try:
		json_data = open(log_path)
		data = json.load(json_data)
		data[element].insert(0,new_completed)
		json_data.close()
	except AttributeError:
		data[element] = [data[element]]
		data[element].insert(0,new_completed)
		json_data.close()
	except KeyError:
		data[element] = [new_completed]
		json_data.close()
	except (IOError, ValueError):
		data = {}
		data[element] = [new_completed]

	dump = json.dumps(data, sort_keys=True,indent=2, separators=(',', ': '))
	if not no_write:
		json_data = open(log_path,"wb")
		json_data.write(dump)
		json_data.close()
	else:
		print dump
	

if __name__ == "__main__":
	main(sys.argv[1:])
