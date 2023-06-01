import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from model import create_tables, Publisher, Book, Shop, Stock, Sale, Base
from connection_data import DSN
def add_data(db_session):
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
            db_session.add(model(id=record.get('pk'), **record.get('fields')))
    db_session.commit()
