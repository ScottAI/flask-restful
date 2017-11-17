import sqlite3
from db import db


class UserModel(db.Model):
    #Table Name
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(80))
    password = db.column(db.String(80))

    # Constructor "should" match SQL Alchemy columns
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "select id, username, password from users where username = ?"
        result = cursor.execute(query, (username,))  # parameters must be in form of tuple
        row = result.fetchone()

        if row:
            user = cls(*row)  # cls is the UserModel Class, i.e. using a class method
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "select id, username, password from users where id = ?"
        result = cursor.execute(query, (_id,))  # parameters must be in form of tuple
        row = result.fetchone()

        if row:
            user = cls(*row)  # cls is the UserModel Class, i.e. using a class method
        else:
            user = None
        connection.close()
        return user