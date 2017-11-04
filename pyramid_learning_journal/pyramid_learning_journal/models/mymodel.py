from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    # DateTime
)

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    title = Column(Text)
    body = Column(Text)
    # creation_date = DateTime.datetime()


Index('my_index', MyModel.name, unique=True, mysql_length=255)
