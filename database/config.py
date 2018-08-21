import os
import urlparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

engine = create_engine('mysql+mysqldb://root:root@localhost/autool', echo=False)
if not database_exists(engine.url):
        create_database(engine.url)

Session = sessionmaker(engine)

session = Session()
