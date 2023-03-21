#!/usr/bin/python3
from cookie import *
from sqlalchemy import desc, asc

Session = sessionmaker(bind=engine)
session = Session()
#Query that returns all the objects in the data base.
#my_cookies = session.query(Cookies).all()
#print(my_cookies.cookie_name)

#for my_cookies in session.query(Cookies):
#    print(my_cookies.__dict__)

#print(session.query(Cookies.cookie_name, Cookies.cookie_recipe_url).first())

#print all the table
'''
for my_cookie in session.query(Cookies):
    print('{:2} - {} - {} - {} - {} - {}'.format(my_cookie.cookie_id,
                                                 my_cookie.cookie_name, my_cookie.cookie_recipe_url,
                                                 my_cookie.cookie_sku, my_cookie.quantity,
                                                 my_cookie.unit_cost))
'''


#ordering
"""
for my_cookie in session.query(Cookies).order_by(Cookies.cookie_id):
    print('{:3} - {}'.format(my_cookie.cookie_id, my_cookie.cookie_name))

"""

#Ordering by DEscending order
for my_cookie in session.query(Cookies).order_by(desc(Cookies.cookie_id)):
    print('{:3} - {}'.format(my_cookie.cookie_id, my_cookie.cookie_name))