from . import BaseModel
from peewee import BooleanField,IntegerField, CharField,ForeignKeyField

class PhoneModel(BaseModel):
    number = IntegerField()

class UserModel(BaseModel):
    name = CharField()
    phone = ForeignKeyField(PhoneModel, backref='users')

class WaitListModel(BaseModel):
    name = CharField()
    is_approved = BooleanField(default=False)
    phone = ForeignKeyField(PhoneModel, backref='waitlists')