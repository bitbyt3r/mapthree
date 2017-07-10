from . import Base

class Space(Base.Base):
  _tablename = "spaces"
  _fields = {
    "name": {"type": "TEXT"},
    "description": {"type": "TEXT"},
  }
