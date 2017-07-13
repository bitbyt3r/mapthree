from .Base import *

class Coordinate(Base):
  _tablename = "coordinates"
  _fields = {
    "loc_x": {"type": REAL},
    "loc_y": {"type": REAL},
    "loc_z": {"type": REAL},
    "rot_x": {"type": REAL},
    "rot_y": {"type": REAL},
    "rot_z": {"type": REAL},
    "sca_x": {"type": REAL},
    "sca_y": {"type": REAL},
    "sca_z": {"type": REAL},
  }
