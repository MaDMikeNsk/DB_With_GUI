from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import User


class DB_Engine:
    def __init__(self):
        self.engine = create_engine('sqlite:///DataBase/users.db', echo=True)
        session = sessionmaker(bind=self.engine)
        self.session = session()

    def insert_user(self, user: User):
        self.session.add(user)
        self.session.commit()

    def delete_user(self, user_id):
        self.session.query(User).filter(User.id == user_id).delete()
        self.session.commit()
