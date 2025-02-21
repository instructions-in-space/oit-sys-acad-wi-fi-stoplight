#!/usr/bin/bash

echo "Welcome to \"monitor.sh\"!  (Press ctrl-c to exit.)"

while : ; do
	latest_line=$(tail -n 1 ../state/web-access-log.txt)
	if [[ "$latest_line" =~ stoplighton ]]; then
		echo on > ../state/current-state.txt
		#echo \"On\" is the current state.
	elif [[ "$latest_line" =~ stoplightoff ]]; then
		echo off > ../state/current-state.txt
		#echo \"Off\" is the current state.
	fi
	sleep 1
done 

# 

