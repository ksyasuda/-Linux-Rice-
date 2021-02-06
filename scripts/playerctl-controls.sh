#!/usr/bin/env bash

set -Eeuo pipefail

if ! $(playerctl status &>/dev/null); then 
	exit 1
fi


ICON=''

get_icon() {
	STATUS=$(playerctl status)
	if [[ $STATUS == "Playing" ]]; then
		ICON=' '
	elif [[ $STATUS == "Paused" ]]; then
		ICON='契 '
	fi
}

while getopts nptsbf options
do
	case $options in
		n)
			playerctl next
			;;
		p)
			playerctl prev
			;;
		t)
			playerctl play-pause
			;;
		s)
			get_icon
			TITLE=$(playerctl metadata title)
			printf "$TITLE\n" | zscroll  --before-text "$ICON" --delay 0.3 --update-check \
				true "playerctl metadata title"
			;;
		b)
			printf "玲\n"
			;;
		f)
			printf "怜\n"
			;;
		?)
			exit 1
			;;
	esac
done
