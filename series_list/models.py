from pony.orm import Database, Required, Set
from . import const


db = Database('sqlite', const.DB_PATH, create_db=True)


class Series(db.Entity):
    """Series item"""
    name = Required(unicode)
    episodes = Set('Episode')


class Episode(db.Entity):
    """Series episode"""
    series = Required(Series)
    season = Required(int)
    number = Required(int)
    name = Required(unicode)


db.generate_mapping(create_tables=True)
