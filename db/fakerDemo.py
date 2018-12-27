# -*- coding: utf-8 -*-

from faker import Faker, Factory
from pymongo import MongoClient
import json
import random

fake = Factory.create(locale='zh_CN')

conn = MongoClient('127.0.0.1', 27017)
db = conn.jsondata
data = db.data
i = 0
while i<1000000:
    num = random.randint(1, 10)
    male = 'M' if num % 2 == 0 else 'F'
    d = {
        'job': fake.job(), 'company': fake.company(), 'ssn': fake.ssn(), 'residence': fake.address(),
        'current_location': fake.location_on_land(coords_only=False),
        'website': [fake.url(schemes=None), fake.url(schemes=None)], 'username': fake.user_name(), 'name': fake.name(),
        'sex': male,
        'address': fake.address(), 'mail': fake.email(), 'birthdate': fake.date(pattern="%Y-%m-%d", end_datetime=None),
        'province': fake.province(), 'street': fake.street_name(),
        'postcode': fake.postcode(), 'color': [fake.safe_color_name(), fake.safe_color_name(), fake.safe_color_name()],
        'credit_card_number': fake.credit_card_number(card_type=None),
        'phone': fake.phone_number()
    }
    data.insert([d])
    i = i+1
