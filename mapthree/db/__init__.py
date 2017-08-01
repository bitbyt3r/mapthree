import records

from .Group_Membership import Group_Membership
from .Arrangement import Arrangement
from .Model_File import Model_File
from .Connection import Connection
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
  Arrangement,
  Model_File,
  Connection,
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
