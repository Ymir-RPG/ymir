from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class World(Base):
    __tablename__ = "worlds"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    def __repr__(self):
        return "<World(name='%s')>" % self.name


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    world_id = Column(Integer, ForeignKey("worlds.id"))
    world = relationship("World", backref=backref("characters", order_by=id))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "world_id": self.world_id,
        }

    def __repr__(self):
        return "<Character(name='%s')>" % self.name


class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    world_id = Column(Integer, ForeignKey("worlds.id"))
    world = relationship("World", backref=backref("places", order_by=id))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "world_id": self.world_id,
        }

    def __repr__(self):
        return "<Place(name='%s')>" % self.name
