"""
Отсда имопртировать либо переменную db_obj либо 2 класса для подключения в другую db или в другогог пользователя
"""


#TODO   Сделать все через либу для flask

import os

from dotenv import load_dotenv, find_dotenv
from mysql.connector import connect, Error
from mysql.connector.connection_cext import CMySQLConnection, CMySQLCursor
from mysql.connector.errors import IntegrityError
from flask import session, Flask

from werkzeug.security import generate_password_hash, check_password_hash # * для хешированного хранения поролей


load_dotenv(find_dotenv())

class GetConnection:
    """
    Class to get connection
    -----------------------
    * Создание поключения юзера к дб

    !!! Все данные юзеров хранить в env файле !!!
    """
    def __init__(
        self, 
        user: str, 
        password: str, 
        host: str,
        db_name: str
    ) -> None:
        self.__user: str = user
        self.__password: str = password
        self.__host: str = host
        self.__db_name: str = db_name
        #TODO брать из env хешированные данные и далле преобразовывать их
        try:
            self.connection: CMySQLConnection = connect(
                host=self.__host,
                user=self.__user,
                database=self.__db_name, #! Будет ошибка при отсутствии БД (Но только в случае рега db на лок пк)
                password=self.__password
            )
    
        except Error as e:
            print(e)
            if e.errno == 1049: # ! Все строчки в execpt для легкой работы в время разработки в дальнейшей эксплуатации удалить
                try:
                    connection: CMySQLConnection = connect(
                        host=self.__host,
                        user=self.__user,
                        password=self.__password,
                    )
                    with connection.cursor() as cursor:
                        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.__db_name};")
                    connection.close()
                    self.connection: CMySQLConnection = connect(
                        host=self.__host,
                        user=self.__user,
                        database=self.__db_name,
                        password=self.__password,
                    )
                except:
                    pass
    def create_hash_data(self):
        pass

    def create_tables(self, cursor: CMySQLCursor):
        #-----Создание таблиц-----
        ...
        #-------------------------

    def create_procedurc(self, cursor: CMySQLCursor):
        #----Создание процедур----
        ...
        #-------------------------
    def create_triggers(self, cursor: CMySQLCursor):
        #---Создание триггеров----
       ...
        #-------------------------
    def add_constant(self, cursor: CMySQLCursor):
        #------------------Заполнение таблиц-констант------------------
        ...
        #--------------------------------------------------------------
            

#TODO Сюда передовать хешированные данные далее в процессе их расхешировать!!!
#! Если подключение более не понадобиться то поставить __ перед переменной !!!
db_obj = DbMethods(
    GetConnection(
        user = os.getenv("user"), 
        password = os.getenv("password"), 
        host = os.getenv("host"),
        db_name = os.getenv("database")
    )
)

# db_obj.connection.cursor().execute(f"DROP DATABASE {db_obj.__conn_obj.db_name}")
# quit()
db_obj.create_db()

# for i in db_obj.get_tables():
#     print(db_obj.get_table_info(i))
