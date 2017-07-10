import records

from .Space import Space

db_types = [Space,]

db = records.Database('sqlite:///mapthree.db')

def init():
  for i in db_types:
    i.init(db)

def register(session):
  for i in db_types:
    i.register(session, db)
