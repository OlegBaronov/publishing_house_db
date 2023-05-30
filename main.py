import sqlalchemy
from sqlalchemy.orm import sessionmaker

from model import create_tables, Publisher, Book, Shop, Stock, Sale, Base
from connection_data import DSN

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()





subq = session.query(Publisher).filter(Publisher.name == input('Имя издателя: ')).subquery()
subq2 = session.query(Book).join(subq, Book.id_publisher == subq.c.id).subquery()
subq3 = session.query(Stock).join(subq2, Stock.id_book == subq2.c.id).subquery()
subq3 = session.query(Stock).join(subq2, Stock.id_book == subq2.c.id).subquery()
q = session.query(Shop).join(subq3, Shop.id == subq3.c.id_shop)















session.close()
























# if __name__ == '__main__':


