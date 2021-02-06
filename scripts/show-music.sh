#!/usr/bin/env bash

set -Eeuo pipefail

## depreciated use zscroll now

# checkRunning=$(mpc current -f '%title% - %artist%' | cut -c -55)
# if [[ $checkRunning == '' ]]; then
# 	exit 1
# fi
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

mpc current | zscroll --before-text "$icon" --delay 0.3 \
		--match-command "mpc status" \
		--match-text "playing" "--before-text ' '" \
		--match-text "paused" "--before-text '契 ' --scroll 0" \
		--update-check true "mpc current" &
wait
