from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ymir import models

engine = create_engine("sqlite:///local.sqlite")
Session = sessionmaker()
Session.configure(bind=engine)
models.Base.metadata.create_all(engine)
session = Session()
