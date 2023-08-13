import os
from flask import g
from peewee import SqliteDatabase, Model, DateField, FloatField


def get_db():
    if 'db' not in g:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        g.db = SqliteDatabase(os.path.join(BASE_DIR, 'app.db'))
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


class BaseModel(Model):
    class Meta:
        database = get_db()
