import sqlalchemy
from sqlalchemy.orm import sessionmaker

from model import create_tables, Publisher, Book, Shop, Stock, Sale, Base
from connection_data import DSN
from task_3 import add_data
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
db_session = Session()


def get_shops(db_session):
    publisher_data = input('Данные публициста: ')
    q = db_session.query(Shop).\
        join(Stock).\
        join(Book).\
        join(Publisher)
    if publisher_data.isdigit() == True:
        result = q.filter(Publisher.id == publisher_data).all()
    else:
        result = q.filter(Publisher.name == publisher_data).all()
    for res in result:
        print(res)



# subq = session.query(Publisher).filter(Publisher.name == input('Имя издателя: ')).subquery()
# subq2 = session.query(Book).join(subq, Book.id_publisher == subq.c.id).subquery()
# subq3 = session.query(Stock).join(subq2, Stock.id_book == subq2.c.id).subquery()
# subq3 = session.query(Stock).join(subq2, Stock.id_book == subq2.c.id).subquery()
# q = session.query(Shop).join(subq3, Shop.id == subq3.c.id_shop)




db_session.close()

if __name__ == '__main__':
    db_session = Session()
    add_data(db_session)
    get_shops(db_session)
