from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Date
)
import datetime
from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    # name = Column(Text)
    title = Column(Text)
    body = Column(Text)
    creation_date = Column(Date)


Index('my_index', MyModel.id, unique=True, mysql_length=255)
