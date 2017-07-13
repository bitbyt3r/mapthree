from .Base import *

class Session(Base):
  _tablename = "sessions"
  _fields = {
    "user_id": {"type": INTEGER},
    "end_time": {"type": DATETIME},
  }
