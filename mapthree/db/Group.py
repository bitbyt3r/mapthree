from .Base import *

class Group(Base):
  _tablename = "groups"
  _fields = {
    "name": {"type": TEXT},
  }
