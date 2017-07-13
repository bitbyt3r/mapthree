from .Base import *

class Entity(Base):
  _tablename = "entities"
  _fields = {
    "name": {"type": TEXT},
    "description": {"type": TEXT},
    "space_id": {"type": INTEGER},
    "model_id": {"type": INTEGER},
    "coordinate_id": {"type": INTEGER},
  }
