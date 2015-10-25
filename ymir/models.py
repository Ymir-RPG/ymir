from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


def date2str(date):
    if date is None:
        return None
    return date.strftime('%Y-%m-%dT%H:%M:%S')


class World(Base):
    __tablename__ = "worlds"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_updated = Column(DateTime)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastUpdated": date2str(self.last_updated),
        }

    def __repr__(self):
        return "<World(name='%s')>" % self.name


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    world_id = Column(Integer, ForeignKey("worlds.id"))
    world = relationship("World", backref=backref("characters", order_by=id))
    place_id = Column(Integer, ForeignKey("places.id"))
    place = relationship("Place", backref=backref("characters", order_by=id))
    last_updated = Column(DateTime)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "worldId": self.world_id,
            "placeId": self.place_id,
            "lastUpdated": date2str(self.last_updated),
        }

    def __repr__(self):
        return "<Character(name='%s')>" % self.name


class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    world_id = Column(Integer, ForeignKey("worlds.id"))
    world = relationship("World", backref=backref("places", order_by=id))
    last_updated = Column(DateTime)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "worldId": self.world_id,
            "lastUpdated": date2str(self.last_updated),
        }

    def __repr__(self):
        return "<Place(name='%s')>" % self.name


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    world_id = Column(Integer, ForeignKey("worlds.id"))
    world = relationship("World", backref=backref("items", order_by=id))
    place_id = Column(Integer, ForeignKey("places.id"))
    place = relationship("Place", backref=backref("items", order_by=id))
    character_id = Column(Integer, ForeignKey("characters.id"))
    character = relationship("Character", backref=backref("items", order_by=id))
    last_updated = Column(DateTime)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "worldId": self.world_id,
            "placeId": self.place_id,
            "characterId": self.character_id,
            "lastUpdated": date2str(self.last_updated),
        }

    def __repr__(self):
        return "<Items(name='%s')>" % self.name
