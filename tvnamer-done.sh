#!/bin/bash
torrentid=$1
torrentname=$2
torrentpath=$3

DIR=/home/pi/torrents/series-b4tvnamer
ANIME_DIR=/home/pi/torrents/anime-b4tvnamer

CONFIG=/home/pi/.tvnamer/config.json 
ANIME_CONFIG=/home/pi/.tvnamer/config.anime.json 

EXEC="python /home/pi/work/tvnamer/tvnamer/main.py"
#EXEC=/usr/local/bin/tvnamer

if [[ "$torrentpath" == *series* ]] || [ -z "$2" ]; then 
	if [ -z "$2" ]
	then
		echo "tvnamer is going to be executed in $DIR"
	else
		echo "tvnamer is going to be executed for $torrentname in $DIR"
	fi
	#
	$EXEC --config=$CONFIG $DIR
else
	echo "series was not found in path: $torrentpath"
fi


if [[ "$torrentpath" == *anime* ]] || [ -z "$2"]; then
	if [ -z "$2" ]
	then
		echo "tvnamer is going to be executed in $ANIME_DIR"
	else
		echo "tvnamer is going to be executed for $torrentname in $ANIME_DIR"
	fi
	#
	$EXEC --config=$ANIME_CONFIG $ANIME_DIR
else
	echo "anime was not found in path: $torrentpath"
fi
