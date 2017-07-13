from .Base import *

class Space(Base):
  _tablename = "spaces"
  _fields = {
    "name": {"type": TEXT},
    "description": {"type": TEXT},
  }
