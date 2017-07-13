from .Base import *

class User(Base):
  _tablename = "users"
  _fields = {
    "name": {"type": TEXT},
  }
