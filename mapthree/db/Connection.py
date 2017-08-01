from .Base import *

class Connection(Base):
  _tablename = "connections"
  _fields = {
    "entitya_id": {"type": INTEGER},
    "entityb_id": {"type": INTEGER},
  }
