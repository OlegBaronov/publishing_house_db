import sqlalchemy
from sqlalchemy.orm import sessionmaker

from model import create_tables, Publisher, Book, Shop, Stock, Sale, Base
from connection_data import DSN

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()





subq = session.query(Publisher).filter(Publisher.name == input('Имя издателя: ')).subquery()

q = session.query(Shop.name).join(Stock.id).join(Book.id_publisher).join(subq, Book.id_publisher == subq.c.id)















session.close()
























# if __name__ == '__main__':


