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

    def to_dict(self):
        """Take all model attributes and render them as a dictionary."""
        return {
               'id': self.id,
               'title': self.title,
               'body': self.body,
               'creation_date': self.creation_date
           }


Index('my_index', MyModel.id, unique=True, mysql_length=255)
