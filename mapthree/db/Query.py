from .Base import *

# Note that this is actually a holder for queries, not a class for performing queries

class Query(Base):
  _tablename = "queries"
  _fields = {
    "name": {"type": TEXT},
    "description": {"type": TEXT},
    "querystring": {"type": TEXT},
  }
