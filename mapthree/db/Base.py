import inspect
from functools import partial

class Base(object):
  _tablename = "if_you_see_this_you_did_not_subclass_base_correctly"
  _fields = {}

  @classmethod
  def register(cls, session, db):
    for i in inspect.getmembers(cls, predicate=inspect.ismethod):
      if i[0].startswith("query_"):
        procedure = "db.{}.{}".format(cls.__name__.lower(), "query_".join(i[0].split("query_")[1:]))
        print("Registering {} as {}".format(i[0], procedure))
        session.session.register(endpoint=partial(i[1], db), procedure=procedure)

  @classmethod
  def init(cls, db):
    key_names = list(cls._fields.keys())
    keys = ", ".join(["{} {}".format(x, cls._fields[x]['type']) for x in key_names])
    db.query('CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, {})'.format(cls._tablename, keys))

  @classmethod
  def query_add(cls, db, *args, **kwargs):
    print("Adding to {}".format(cls._tablename))
    keys = list(cls._fields.keys())
    key_names = ", ".join(keys)
    key_formats = ", ".join([":"+x for x in keys])
    db.query('INSERT INTO {} ({}) VALUES({})'.format(cls._tablename, key_names, key_formats), **kwargs)

  @classmethod
  def query_delete(cls, db, id):
    print("Deleting {} from {}".format(id, cls._tablename))
    db.query('DELETE FROM {} WHERE id = :id'.format(cls._tablename), id=id)

  @classmethod
  def query_update(cls, db, id, **kwargs):
    print("Updating {} in {}".format(id, cls._tablename))
    keys = list(kwargs.keys())
    values = ", ".join(["{}={}".format(x, y) for x,y in kwarg])
    db.query('UPDATE {} SET {} WHERE id = :id'.format(cls._tablename, values), id=id)

  @classmethod
  def query_get(cls, db, id):
    print("Getting {} from {}".format(id, cls._tablename))
    return db.query("SELECT * FROM {} WHERE id = :id".format(cls._tablename), id=id).export('json')

  @classmethod
  def query_get_all(cls, db):
    print("Getting all from {}".format(cls._tablename))
    return db.query("SELECT * FROM {}".format(cls._tablename)).export('json')


