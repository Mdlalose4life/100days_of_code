#!/usr/bin/python3
from cookie import *
# Let's update the number of Votex cookies.
Session = sessionmaker(bind=engine)
session = Session()

query = session.query(Cookies)
vc_cookies = query.filter(Cookies.cookie_name == 'Vortex_chip').first()
vc_cookies.quantity = vc_cookies.quantity - 1
session.commit()
print(vc_cookies.quantity)

Tc_cookies = query.filter(Cookies.cookie_name == 'Tricky_chip').first()
Tc_cookies.quantity = Tc_cookies.quantity - 1
session.commit()
print(Tc_cookies.quantity)