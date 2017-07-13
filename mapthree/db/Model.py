from .Base import *

class Model(Base):
  _tablename = "models"
  _fields = {
    "name": {"type": TEXT},
    "description": {"type": TEXT},
    "space_id": {"type": INTEGER},
    "format": {"type": INTEGER},
  }
