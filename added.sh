#!/bin/sh
torrentname=$2

ELEMENT=added

RCFILE=~/.deluge-commandsrc
if [ -f $RCFILE ]; then
	. $RCFILE
else
	echo "please create $RCFILE"
	echo "\t(see deluge-commandsrc.example)"
	return
fi

# runs script that actually updates log file
$SCRIPT --log_path "$LOG_FILE" --element "$ELEMENT" --torrentname "$torrentname" 
# uploads logfile to dropbox
$EXEC upload "$LOG_FILE" "$DROPBOX"
