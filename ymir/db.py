import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ymir import models


def get_session(db_conn_str=None):
    if not db_conn_str:
        db_conn_str = os.environ.get("YMIR_DB_CONN_STR",
                                     "sqlite:///local.sqlite")
    engine = create_engine(db_conn_str)
    Session = sessionmaker()
    Session.configure(bind=engine)
    models.Base.metadata.create_all(engine)
    return Session()
