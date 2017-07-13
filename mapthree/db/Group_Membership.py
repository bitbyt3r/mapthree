from .Base import *

class Group_Membership(Base):
  _tablename = "group_memberships"
  _fields = {
    "user_id": {"type": INTEGER},
    "group_id": {"type": INTEGER},
  }
