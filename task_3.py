import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from model import create_tables, Publisher, Book, Shop, Stock, Sale, Base
from connection_data import DSN
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

with open('tests_data.json', 'r') as fd:
    data = json.load(fd)
for record in data:
    model = {
    'publisher': Publisher,
    'shop': Shop,
    'book': Book,
    'stock': Stock,
    'sale': Sale
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))

    session.commit()




    session.close()