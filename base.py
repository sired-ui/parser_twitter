from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.inspection import inspect

DB_PATH = "sqlite:///./db.db"
engine = create_engine(DB_PATH, connect_args={"check_same_thread": False})


Base = declarative_base()


class Account(Base):
    __tablename__ = "accounts"
 
    id = Column(Integer, primary_key=True, index=True)
    twitter_id = Column(Integer)
    name = Column(String)
    username = Column(String)
    following_count = Column(Integer)
    followers_count = Column(Integer)
    description = Column(String)


class Statuses(Base):
	__tablename__ = "statuses"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String)


class Sessions(Base):
	__tablename__ = "sessions"

	id = Column(Integer, primary_key=True, index=True)
	session_id = Column(Integer)
	username = Column(String)
	status = Column(Integer)


class Conf(Base):
	__tablename__ = "conf"

	id = Column(Integer, primary_key=True, index=True)
	session_id = Column(Integer)


def get_session(session_id):
	elements = read_db.query(Sessions).filter_by(session_id=session_id)
	data = []
	for el in elements:
		status = read_db.get(Statuses,el.status).name
		data.append({"username":el.username,"status":status})
	return data


def get_user_data(username):
	user = read_db.query(Account).filter_by(username=username).first()
	return {"twitter_id": user.twitter_id, "name": user.name, "username": user.username, "following_count": user.following_count, "followers_count": user.followers_count, "description": user.description}


SessionLocal = sessionmaker(autoflush=False, bind=engine)
ReadSession = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()
read_db = ReadSession()