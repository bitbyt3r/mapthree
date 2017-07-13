from functools import partial
import autobahn_sync
import requests
import time
import db

wamp = autobahn_sync.AutobahnSync()

_callbacks = []

def register_callbacks():
  print("Registering main functions...")
  for i in _callbacks:
    print("Registering {}".format(i['procedure']))
    wamp.session.register(endpoint=i['endpoint'], procedure=i['procedure'])

def register(func, procedure=None):
  if not procedure:
    procedure = func.__name__
  _callbacks.append({'endpoint': func, 'procedure': procedure})
  return func

@register
def run_query(query):
  headers = {"Content-Type": "application/json"}
  r = requests.post('http://localhost:5000/query', data=query, headers=headers)
  return r.text

db.init()
wamp._on_running_callbacks.append(partial(db.register, wamp))
wamp._on_running_callbacks.append(register_callbacks)
wamp.run(url='ws://localhost:8888/ws', realm='realm1', blocking=True)
