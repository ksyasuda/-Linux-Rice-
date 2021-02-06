#!/usr/bin/env bash

## depreciated use zscroll now

checkRunning=$(mpc current)
if [[ $checkRunning == '' ]]; then
	exit 1
fi
# 
# checkPlaying=$(mpc status | grep playing)
# icon=''
# if [[ $checkPlaying == '' ]]; then
# 	icon='契'
# else
# 	icon=''
# fi
# echo $icon $checkRunning
# "契"
# ""
# "玲"
# "怜"

mpc current | zscroll --delay 0.3 \
		--match-command "mpc status" \
		--match-text "playing" "--before-text ' '" \
		--match-text "paused" "--before-text '契 ' --scroll 0" \
		--update-check true "mpc current" &
wait
