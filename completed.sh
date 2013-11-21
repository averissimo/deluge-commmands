#!/bin/bash
torrentname=$2

TO=1 # 0 for added 1 for completed

PARENT=/home/pi/torrents
LOG_ADDED_FILE=$PARENT/added.log
LOG_COMPLETED_FILE=$PARENT/completed.log

DROPBOX=framboesa

EXEC=/home/pi/work/Dropbox-Uploader/dropbox_uploader.sh
SCRIPT="python /home/pi/work/deluge-commands/deluge-json.py"

if [ $TO = 0 ] ; then
	UPLOAD_FILE=$LOG_ADDED_FILE
else
	UPLOAD_FILE=$LOG_COMPLETED_FILE
fi

# runs script that actually updates log file
$SCRIPT --torrentname $torrentname --log_path $UPLOAD_FILE

# uploads logfile to dropbox
$EXEC upload "$UPLOAD_FILE" "$DROPBOX"


