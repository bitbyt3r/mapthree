from .Base import *

# An arrangement is a query in a space
class Arrangement(Base):
  _tablename = "arrangements"
  _fields = {
    "name": {"type": TEXT},
    "description": {"type": TEXT},
    "space_id": {"type": INTEGER},
    "query_id": {"type": INTEGER},
  }
