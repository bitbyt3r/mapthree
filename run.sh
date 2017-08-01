#!/usr/bin/bash
trap 'kill $(jobs -p)' EXIT

npm run dev &
/opt/crossbar/bin/pypy /opt/crossbar/bin/crossbar start &
sleep 5
source mapthree/venv/bin/activate
python3 mapthree/server.py

