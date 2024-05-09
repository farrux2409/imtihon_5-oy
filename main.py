# Yo`ldashov Farrux
from typing import List

# 1-Question
# 1 - version
import psycopg2

user = 'postgres'
host = 'localhost'
password = '123'
database = 'n42'
port = 5432

conn = psycopg2.connect(user=user, host=host, password=password, database=database)
cur = conn.cursor()


def create_table():
    create_table_query = ''' create table if not exists Product(
    id serial primary key,
    name varchar(30) not null,
    price int not null,
    color varchar(30) not null,
    image varchar(100) not null);'''
    cur.execute(create_table_query)
    print('Successfully created')


create_table()
# 2-version

db_params: dict = {
    'user': 'postgres',
    'host': 'localhost',
    'database': 'n42',
    'password': '123',
    'port': 5432

}


class DbConnect:
    def __init__(self, db__params: dict):
        self.db_params = db__params
        self.conn = psycopg2.connect(**self.db_params)

    def __enter__(self):
        self.cur = conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur and not self.cur.closed:
            self.conn.commit()
            self.cur.close()
            self.conn.close()


class Products:
    def __init__(self,
                 id: int | None = None,
                 name: str | None = None,
                 price: int | None = None,
                 color: str | None = None,
                 image: str | None = None):
        self.id = id
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def create_table1(self):
        with DbConnect(db_params) as cur1:
            create_table_query = ''' create table if not exists Product(
               id serial primary key,
               name varchar(30) not null,
               price int not null,
               color varchar(30) not null,
               image varchar(100) not null);'''
            cur1.execute(create_table_query)
            print('Successfully created')

    def insert_table(self):
        with DbConnect(db_params) as cur1:
            insert_table_query = ''' insert table Product(name,price,color,image) values(%s,%s,%s,%s)'''
        insertable_params = (self.name, self.price, self.color, self.image)
        cur1.execute(insert_table_query, insertable_params)
        print('INSERT 0 1')


product = Products(name='Phone', price=200, color='black')
product.insert_table()


# 2-Question

def insert_product(name, price, color, image):
    insert_table_query = ''' insert table Product(name,price,color,image) values(%s,%s,%s,%s)'''
    insert_table_params = (name, price, color, image)
    cur.execute(insert_table_query, insert_table_params)
    conn.commit()
    print('INSERT 0 1')


insert_product('Phone', 23232, 'black', 'asasasa')


def select_all():
    select_all_query = '''select * from Product;'''
    cur.execute(select_all_query)
    for i in cur.fetchall():
        print(i)


#
# def delete_pro():
#     delete_table_query = '''delete * from Product where id = %s'''
#     _id: int = int(input('Enter id:  '))
#     cur.execute(delete_table_query, (_id,))
#     print('Successfully deleted')


# delete_pro()


def update_table():
    name = input('Enter name: ')
    id = int(input('Enter id: '))
    update_table_query = ''' update Product set name = %s where id  = %s'''
    update_table_params = (name, id)
    cur.execute(update_table_query, update_table_params)
    conn.commit()


# update_table()

# 3-Question
class Alphabet:
    def __init__(self, letters: List):
        self.index = 0
        self.letters = letters

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.letters):
            raise StopIteration
        else:
            result = self.letters[self.index]
            self.index += 1
            return result


my_words = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X',
            'Y', 'Z', 'SH', 'CH', 'NG']

alphabet = Alphabet(my_words)

# 1-version ------
# print(next(alphabet))
# print(next(alphabet))
# print(next(alphabet))
# print(next(alphabet))
# print(next(alphabet))
# print(next(alphabet))
# print(next(alphabet))
# print(next(alphabet))
#
# while True:
#     try:
#         print(next(alphabet))
#     except StopIteration as e:
#         break

# 2-version ----------
# for i in alphabet:
#     print(i)

# 4-Question

import time


def print_numbers():
    for i in range(1, 6):
        # print(f'numbers =>{i}')
        time.sleep(1)


def print_letters():
    arr = ['One', 'Two', 'Three', 'Fourth', 'Five', 'Six']
    for i in arr:
        # print(f'letter =>{i}')
        time.sleep(1)


# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
#
# start = time.time()

# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()

# 5-Question


db_params: dict = {
    'user': 'postgres',
    'host': 'localhost',
    'database': 'n42',
    'password': '123',
    'port': 5432

}


class DbConnect:
    def __init__(self, db__params: dict):
        self.db_params = db__params
        self.conn = psycopg2.connect(**self.db_params)

    def __enter__(self):
        self.cur = conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur and not self.cur.closed:
            self.conn.commit()
            self.cur.close()
            self.conn.close()


class Products:
    def __init__(self,
                 id: int | None = None,
                 name: str | None = None,
                 price: int | None = None,
                 color: str | None = None,
                 image: str | None = None):
        self.id = id
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def create_table1(self):
        with DbConnect(db_params) as cur1:
            create_table_query = ''' create table if not exists Product(
               id serial primary key,
               name varchar(30) not null,
               price int not null,
               color varchar(30) not null,
               image varchar(100) not null);'''
            cur1.execute(create_table_query)
            print('Successfully created')

    def insert_table(self):
        with DbConnect(db_params) as cur1:
            insert_table_query = ''' insert table Product(name,price,color,image) values(%s,%s,%s,%s)'''
        insertable_params = (self.name, self.price, self.color, self.image)
        cur1.execute(insert_table_query, insertable_params)
        print('INSERT 0 1')


product = Products(name='Phone', price=200, color='black')
product.create_table1()
product.insert_table()


# 6-Question


class DbConnect:
    def __init__(self, db__params: dict):
        self.db_params = db__params
        self.conn = psycopg2.connect(**self.db_params)

    def __enter__(self):
        self.cur = conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur and not self.cur.closed:
            self.conn.commit()
            self.cur.close()
            self.conn.close()


class Products:
    def __init__(self,
                 id: int | None = None,
                 name: str | None = None,
                 price: int | None = None,
                 color: str | None = None,
                 image: str | None = None):
        self.id = id
        self.name = name
        self.price = price
        self.color = color
        self.image = image


# extra examples ---------------
# with Iterators
class Fibonacci:
    def __init__(self, stop):
        self.current = 0
        self.index = 0
        self.next = 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.stop:
            fibonacci_num = self.current
            self.index += 1
            self.current, self.next = self.next, self.current + self.next
            return fibonacci_num
        else:
            raise StopIteration


fibonacci = Fibonacci(9)


# # 1-version
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
#
# while True:
#     try:
#         print(next(fibonacci))
#     except  StopIteration as e:
#         break

# 2-version

# for i in fibonacci:
#     print(i)

# with generators
def fibonacci1(stop: int):
    prev, current = 0, 1
    index = 0
    while index < stop:
        yield prev
        prev, current = current, prev + current
        index += 1


fibonacci2 = fibonacci1(9)

# 1-version

# print(next(fibonacci2))
# print(next(fibonacci2))
# print(next(fibonacci2))
# print(next(fibonacci2))
# print(next(fibonacci2))

# while True:
#     try:
#         print(next(fibonacci2))
#     except StopIteration as e:
#         break

# 2-version

for i in fibonacci2:
    print(i)
