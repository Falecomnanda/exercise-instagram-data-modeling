import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
class Follower(Base):
    __tablename__ = 'followers'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    user = relationship(User)
    follower_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    follower = relationship(User)
class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    email = Column(String(200), nullable=False)
    biogra = Column(String(255), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)
class avatar(Base):
    __tablename__ = 'avatars'
    id = Column(Integer, primary_key=True)
    avatar = Column(String(200), nullable=True)
    profile_id = Column(Integer, ForeignKey('profiles.id'))
    profile = relationship(Profile)






## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')