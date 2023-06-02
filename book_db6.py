import sqlalchemy
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Shop, Book, Stock, Sale

DNC = "postgresql://postgres:123456@localhost:5432/book_db"
engine = sqlalchemy.create_engine(DNC)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher_1 = Publisher(name="Eduction")
publisher_2 = Publisher(name="White Star")
publisher_3 = Publisher(name="AST")
session.add_all([publisher_1, publisher_2, publisher_3])

shop_1 = Shop(name="Буквоед")
shop_2 = Shop(name="Дом Книги")
shop_3 = Shop(name="Читай Город")
session.add_all([shop_1, shop_2, shop_3])

book_1 = Book(title="Черный город", id_publisher=1)
book_2 = Book(title="Война и мир", id_publisher=1)
book_3 = Book(title="Мастер и Маргарита", id_publisher=2)
book_4 = Book(title="Смерть Ахилеса", id_publisher=3)
book_5 = Book(title="Не прощаюсь", id_publisher=3)
session.add_all([book_1, book_2, book_3, book_4, book_5])


stock_1 = Stock(id_shop=1, id_book=1, count=500)
stock_2 = Stock(id_shop=1, id_book=2, count=600)
stock_3 = Stock(id_shop=1, id_book=2, count=700)
stock_4 = Stock(id_shop=2, id_book=1, count=800)
stock_5 = Stock(id_shop=2, id_book=1, count=900)
stock_6 = Stock(id_shop=2, id_book=3, count=100)
stock_7 = Stock(id_shop=3, id_book=2, count=200)
stock_8 = Stock(id_shop=3, id_book=3, count=300)
session.add_all([stock_1, stock_2, stock_3, stock_4, stock_5, stock_6, stock_7, stock_8])

sale_1 = Sale(price=1000.99, date_sale="2022-06-23", id_stock=1, count=10)
sale_2 = Sale(price=1200.99, date_sale="2022-06-22", id_stock=2, count=20)
sale_3 = Sale(price=1500.99, date_sale="2022-06-21", id_stock=3, count=30)
sale_4 = Sale(price=1900.99, date_sale="2022-06-20", id_stock=4, count=40)
sale_5 = Sale(price=2000.99, date_sale="2022-06-19", id_stock=5, count=50)
sale_6 = Sale(price=1100.99, date_sale="2022-06-19", id_stock=6, count=60)
sale_7 = Sale(price=1300.99, date_sale="2022-06-18", id_stock=7, count=70)
sale_8 = Sale(price=1400.99, date_sale="2022-06-17", id_stock=8, count=80)
session.add_all([sale_1, sale_2, sale_3, sale_4, sale_5, sale_6, sale_7, sale_8])

session.commit()
session.close()


q = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.name == input("Введите издателя"))

for s in q.all():
    print([s[0]] + [s[1]] + [str(s[2])] + [str(s[3])])





