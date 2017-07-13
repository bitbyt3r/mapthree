from .Base import *

# This is used for all files associated with a model, including textures

class Model_File(Base):
  _tablename = "model_files"
  _fields = {
    "name": {"type": TEXT},
    "model_id": {"type": INTEGER},
    "location": {"type": TEXT},
  }
