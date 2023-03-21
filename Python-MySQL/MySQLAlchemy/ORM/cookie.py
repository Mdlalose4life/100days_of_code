#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, Numeric, String,ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy import DateTime

#Creating an Enging
engine = create_engine('mysql://root:admin@localhost/Cookie_Store', echo=False)

#Creating an instance of a declarative base
Base = declarative_base()

# Cookie class inherits the declarative base.
class Cookies(Base):
    #defines the table name
    __tablename__ = 'my_cookies'

    #Define Atriutes of th table and the set at least one primary key.
    cookie_id = Column(Integer(), primary_key=True)
    cookie_name = Column(String(255), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12,2))
'''
class Users(Base):
    __tablename__ = 'Users'

    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    email_address = Column(String(255), nullable=False)
    phone = Column(String(25), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

class Orders(Base):
    __tablename__ = 'Orders'

    order_id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.user.id'))
    shipped = Column(Boolean(), default=False)

class line_items(Base):
    __tablename__ = 'Line_items'
    
    line_Items_id = Column(Integer(), primary_key=True)
    order_id = Column(ForeignKey('orders.order_id'))
    cookie_id = Column(ForeignKey('cookies.cookies_id'))

Session = sessionmaker(bind=engine)
session = Session()

cc_cookie = Cookies(cookie_name='Creamy_chip',
                       cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
                       cookie_sku = 'CC01',
                       quantity=12,
                       unit_cost=0.50)

dc_cookie = Cookies(cookie_name='Dark_chip',
                       cookie_recipe_url='http://some.dark/cookie/recipe.html',
                       cookie_sku = 'CC201',
                       quantity=15,
                       unit_cost=0.70)
sc_cookie = Cookies(cookie_name='Sick_chip',
                       cookie_recipe_url='http://somesick/cookie/recipe.html',
                       cookie_sku = 'CC20',
                       quantity=18,
                       unit_cost=0.58)
vc_cookie = Cookies(cookie_name='Vortex_chip',
                       cookie_recipe_url='http://some.votex/cookie/recipe.html',
                       cookie_sku = 'CC25',
                       quantity=74,
                       unit_cost=0.20)
Vc_cookie = Cookies(cookie_name='Virus_chip',
                       cookie_recipe_url='http://some.votex/cookie/recipe.html',
                       cookie_sku = 'CC26',
                       quantity=74,
                       unit_cost=0.23)
xc_cookie = Cookies(cookie_name='X_chip',
                       cookie_recipe_url='http://some.votex/cookie/recipe.html',
                       cookie_sku = 'CC27',
                       quantity=74,
                       unit_cost=0.12)
Tc_cookie = Cookies(cookie_name='Tricky_chip',
                       cookie_recipe_url='http://some.votex/cookie/recipe.html',
                       cookie_sku = 'CC28',
                       quantity=74,
                       unit_cost=0.21)
Ac_cookie = Cookies(cookie_name='African_chip',
                       cookie_recipe_url='http://some.votex/cookie/recipe.html',
                       cookie_sku = 'CC29',
                       quantity=74,
                       unit_cost=0.15)

session.add(cc_cookie)
session.add(dc_cookie)
session.add(sc_cookie)
session.add(vc_cookie)
session.add(Vc_cookie)
session.add(Tc_cookie)
session.commit()
'''
Base.metadata.create_all(engine)