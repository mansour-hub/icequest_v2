from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
        __tablename__='user'
        user_id = Column(Integer, primary_key = True)
        name = Column(String)
        surname = Column(String)
        phone = Column(String)
        date = Column(String)
        nationality = Column(String)
        email = Column(String)
        playing = Column(Boolean, default = False)

        def __repr__(self):
        	return("<id: {}, name: {}, surname: {}, phone num: {}, date: {}, nationality: {}, email: {}, playing: {}>").format(
                               self.user_id,
                               self.name,
                               self.surname,
                               self.phone,
                               self.date,
                               self.nationality,
                               self.email,
                               self.playing)



