from .Base import *

class Entity(Base):
  _tablename = "entities"
  _fields = {
    "name": {"type": TEXT},
    "description": {"type": TEXT},
    "type": {"type": TEXT},
    "space_id": {"type": INTEGER},
    "model_id": {"type": INTEGER},
    "coordinate_id": {"type": INTEGER},
    "parent_id": {"type": INTEGER},
  }
