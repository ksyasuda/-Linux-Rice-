#!/usr/bin/env bash

set -Eeuo pipefail

# check to see if there is anything playing
# if not program exits I think
player=$(playerctl status 1>/dev/null 2>/dev/null) 
if [[ $# -ne 1 ]]; then
	echo 'You must append either the "prev" or "append" argument'
	exit 1
fi

# argument, which decides which icon to print
arg=$1
if [[ $arg == 'prev' ]]; then
	echo "玲"
elif [[ $arg == 'next' ]]; then
	echo "怜"
fi
