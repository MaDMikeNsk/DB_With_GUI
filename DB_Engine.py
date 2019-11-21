from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import User
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DB_Engine:
    def __init__(self):
        self.engine = create_engine('sqlite:///DataBase/users.db', echo=True)
        session = sessionmaker(bind=self.engine)
        self.session = session()

    def insert_user(self, user: User):
        self.session.add(user)
        self.session.commit()

    def delete_user(self, user_id):
        instance = self.session.query(User).filter(User.id == user_id).first()
        self.session.delete(instance)
        self.session.commit()
