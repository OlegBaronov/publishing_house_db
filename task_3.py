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
    pb1 = Publisher(name="publisher")
    sh1 = Shop(name="name")
    bk1 = Book(title="title", id_publisher="id_publisher")
    st1 = Stock(id_book="id_book", id_shop="id_shop", count="count")
    sl1 = Sale(price="price", date_sale="date_sale", id_stock="id_stock", count="count")





    session.close()