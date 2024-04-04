#!/bin/sh
URL=${URL:-http://127.0.0.1:4000/health-a}
TIMEOUT=${TIMEOUT:-2}

while true ; do
	printf "%s" "$(date +%T) .. "
	curl -sS --max-time "$TIMEOUT" "$URL"
	sleep 1
done
