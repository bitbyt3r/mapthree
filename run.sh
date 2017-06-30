#!/usr/bin/bash
trap 'kill $(jobs -p)' EXIT

npm run dev &
/opt/crossbar/bin/pypy /opt/crossbar/bin/crossbar start &
python3 mapthree/server.py

