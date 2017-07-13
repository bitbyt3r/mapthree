import records

from .Group_Membership import Group_Membership
from .Model_File import Model_File
from .Coordinate import Coordinate
from .Session import Session
from .Entity import Entity
from .Model import Model
from .Space import Space
from .Query import Query
from .Group import Group
from .User import User

db_types = [
  Group_Membership,
  Model_File,
  Coordinate,
  Session,
  Entity,
  Model,
  Space,
  Query,
  Group,
  User,
]

db = records.Database('sqlite:///mapthree.db')

def init():
  for i in db_types:
    i.init(db)

def register(session):
  for i in db_types:
    i.register(session, db)
