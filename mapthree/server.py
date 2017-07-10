from functools import partial
import autobahn_sync
import time
import db

wamp = autobahn_sync.AutobahnSync()

db.init()
wamp._on_running_callbacks.append(partial(db.register, wamp))

wamp.run(url='ws://localhost:8888/ws', realm='realm1', blocking=True)
