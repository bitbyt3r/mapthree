#!/usr/bin/env python3
import autobahn_sync
import readline
import json
import re

wamp = autobahn_sync.AutobahnSync()
wamp.run(url='ws://localhost:8888/ws', realm='realm1')

while True:
  try:
    query = input(":")
    m = re.search('^(\'.*\')\s*(\[.*\])?\s*(\{.*\})?$', query)
    parts = m.groups()
    args = []
    kwargs = {}
    if parts[0]:
      function = parts[0].split("'")[1]
    if parts[1]:
      args = json.loads(parts[1])
    if parts[2]:
      kwargs = json.loads(parts[2])
    print(wamp.session.call(function, *args, **kwargs))
  except Exception as e:
    print(e)
