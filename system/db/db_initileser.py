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
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS types(
                id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
                t_name VARCHAR(20) NOT NULL UNIQUE,
                PRIMARY KEY(id)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS m_statuses(
                id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
                s_name VARCHAR(20) NOT NULL UNIQUE,
                PRIMARY KEY(id)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS t_statuses(
                id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
                s_name VARCHAR(20) NOT NULL UNIQUE,
                PRIMARY KEY(id)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS d_statuses(
                id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
                s_name VARCHAR(20) NOT NULL UNIQUE,
                PRIMARY KEY(id)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS roles(
                id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
                role_name VARCHAR(255),
                PRIMARY KEY(id)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
                u_email VARCHAR(100) NOT NULL UNIQUE,
                u_name VARCHAR(100) NOT NULL UNIQUE,
                u_pass CHAR(200) NOT NULL,
                cost_per_hour MEDIUMINT UNSIGNED,
                r_id TINYINT UNSIGNED NOT NULL,
                PRIMARY KEY(id),
                INDEX(r_id), FOREIGN KEY (r_id) REFERENCES roles(id),
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tehno_park(
                id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
                t_name VARCHAR(100) NOT NULL UNIQUE,
                description TEXT,
                moto_hours INT UNSIGNED,
                fuil TINYINT (3) ZEROFILL UNSIGNED,
                s_id TINYINT UNSIGNED NOT NULL,
                PRIMARY KEY(id),
                INDEX(s_id), FOREIGN KEY (s_id) REFERENCES t_statuses(id)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """)        #! fuil переделать в float 
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS images(
                id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                obj_id MEDIUMINT UNSIGNED NOT NULL,
                obj_url VARCHAR(225) NOT NULL UNIQUE,
                PRIMARY KEY(id),
                INDEX(obj_id),
                FOREIGN KEY (obj_id) REFERENCES users(id),
                FOREIGN KEY (obj_id) REFERENCES tehno_park(id)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tehno(
                id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                t_id TINYINT UNSIGNED NOT NULL,
                tehno_id MEDIUMINT UNSIGNED NOT NULL,
                u_id MEDIUMINT UNSIGNED NOT NULL,
                time_count INT UNSIGNED,
                comment TEXT,
                PRIMARY KEY(id),
                INDEX(t_id), FOREIGN KEY (t_id) REFERENCES types(id),
                INDEX(tehno_id), FOREIGN KEY (tehno_id) REFERENCES tehno_park(id),
                INDEX(u_id), FOREIGN KEY (u_id) REFERENCES users(id)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS detali(
                id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
                d_name VARCHAR(20) NOT NULL UNIQUE,
                d_count INT UNSIGNED NOT NULL,
                d_coast INT UNSIGNED NOT NULL,
                PRIMARY KEY(id)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS detali_tehno(
                id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
                d_id TINYINT UNSIGNED NOT NULL,
                t_id BIGINT UNSIGNED NOT NULL,
                d_count INT UNSIGNED NOT NULL,
                PRIMARY KEY(id),
                INDEX(d_id), FOREIGN KEY (d_id) REFERENCES detali(id),
                INDEX(t_id), FOREIGN KEY (t_id) REFERENCES tehno(id)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS members(
                id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                u_id MEDIUMINT UNSIGNED NOT NULL,
                fullname varchar(255) NOT NULL,
                phone VARCHAR(15) NOT NULL UNIQUE,
                s_id TINYINT UNSIGNED NOT NULL,
                description TEXT,
                PRIMARY KEY(id),
                INDEX(u_id), FOREIGN KEY (u_id) REFERENCES users(id),
                INDEX(s_id), FOREIGN KEY (s_id) REFERENCES m_statuses(id)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """)    # ? coast_deal спросить может перенести в deal ибо мембер 1 а дел много уже сделал
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS deal(
                id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                m_id MEDIUMINT UNSIGNED NOT NULL,
                u_id MEDIUMINT UNSIGNED NOT NULL,
                s_id TINYINT UNSIGNED NOT NULL,
                coast_deal INT UNSIGNED NOT NULL,
                PRIMARY KEY(id),
                INDEX(m_id), FOREIGN KEY (m_id) REFERENCES members(id),
                INDEX(u_id), FOREIGN KEY (u_id) REFERENCES users(id),
                INDEX(s_id), FOREIGN KEY (s_id) REFERENCES d_status(id)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS deal_action(
                id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
                d_id MEDIUMINT UNSIGNED NOT NULL,
                description TEXT,
                t_id INT UNSIGNED,
                s_id TINYINT UNSIGNED NOT NULL,
                PRIMARY KEY(id),
                INDEX(d_id), FOREIGN KEY (d_id) REFERENCES deal(id),
                INDEX(t_id), FOREIGN KEY (t_id) REFERENCES tasks(id),
                INDEX(s_id), FOREIGN KEY (s_id) REFERENCES d_statuses(id)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
                id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
                u_id MEDIUMINT UNSIGNED NOT NULL,
                task TEXT NOT NULL,
                dedline DATE,
                s_id TINYINT UNSIGNED NOT NULL,
                PRIMARY KEY(id),
                INDEX(u_id), FOREIGN KEY (u_id) REFERENCES users(id),
                INDEX(s_id), FOREIGN KEY (s_id) REFERENCES d_statuses(id)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """)
        #-------------------------

    def create_procedurc(self, cursor: CMySQLCursor):
        #----Создание процедур----
        #? Спросить может ли быть у разных пользователей 1 и тот же номер телефона !
        #? Спросить добвляем по user'a по id или по любому другому параметру !
        cursor.execute(f"""
            CREATE DEFINER='{self.__user}'@'{self.__host}' PROCEDURE IF NOT EXISTS add_member(
                IN p_u_id MEDIUMINT,
                IN p_fullname VARCHAR(100),
                IN p_phone VARCHAR(20),
                IN p_status TINYINT,
                IN p_description TEXT
            )
            BEGIN
                if ( SELECT EXISTS (SELECT 1 FROM members WHERE p_phone = phone LIMIT 1) ) THEN
                    SELECT 'Member Exists !!';
                ELSE
                    INSERT INTO members
                    (
                        u_id,
                        fullname,
                        phone,
                        s_id,
                        description
                    )
                    VALUES
                    (
                        p_u_id,
                        p_fullname,
                        p_phone,
                        (SELECT id FROM m_statuses WHERE status = p_status LIMIT 1),
                        description
                        
                    );
                END IF;
            END
        """)
        cursor.execute(f"""
            CREATE DEFINER='{self.__user}'@'{self.__host}' PROCEDURE IF NOT EXISTS add_deal_action(
                IN p_d_id MEDIUMINT,
                IN p_description TEXT,
                IN p_t_id VARCHAR(20),
                IN p_status TINYINT
            )
            BEGIN
                if ( SELECT EXISTS (SELECT 1 FROM members WHERE p_phone = phone LIMIT 1) ) THEN
                    SELECT 'Member Exists !!';
                ELSE
                    INSERT INTO members
                    (
                        d_id,
                        description,
                        t_id,
                        s_id
                    )
                    VALUES
                    (
                        p_d_id,
                        p_description,
                        p_t_id,
                        (SELECT id FROM m_statuses WHERE status = p_status LIMIT 1),
                        
                    );
                END IF;
            END
        """)
        #? Обговорить что мы получаем что передаем!!!
        cursor.execute(f"""
            CREATE DEFINER='{self.__user}'@'{self.__host}' PROCEDURE IF NOT EXISTS add_deal(
                IN p_m_id MEDIUMINT,
                IN p_u_id MEDIUMINT,
                IN p_status TINYINT,
                IN p_coast_deal INT
            )
            BEGIN
                if ( SELECT EXISTS (SELECT 1 FROM members WHERE p_phone = phone LIMIT 1) ) THEN
                    SELECT 'Member Exists !!';
                ELSE
                    INSERT INTO members
                    (
                        m_id,
                        u_id,
                        s_id,
                        coast_deal
                    )
                    VALUES
                    (
                        p_m_id,
                        p_u_id,
                        (SELECT id FROM d_statuses WHERE status = p_status LIMIT 1),
                        p_coast_deal

                    );
                END IF;
            END
        """)
        cursor.execute(f"""
            CREATE DEFINER='{self.__user}'@'{self.__host}' PROCEDURE IF NOT EXISTS add_task(
                IN p_u_id MEDIUMINT,
                IN p_task TEXT,
                IN p_dedline DATE,
                IN p_status TINYINT
            )
            BEGIN
                if ( SELECT EXISTS (SELECT 1 FROM members WHERE p_phone = phone LIMIT 1) ) THEN
                    SELECT 'Task Exists !!';
                ELSE
                    INSERT INTO members
                    (
                        u_id,
                        task,
                        dedline,
                        s_id
                    )
                    VALUES
                    (
                        p_u_id,
                        p_task,
                        p_dedline,
                        (SELECT id FROM d_statuses WHERE status = p_status LIMIT 1)
                        
                    );
                END IF;
            END
        """)
        cursor.execute(f"""
            CREATE DEFINER='{self.__user}'@'{self.__host}' PROCEDURE IF NOT EXISTS user_registration(
                IN p_email VARCHAR(100),
                IN p_name VARCHAR(100),
                IN p_pass CHAR(200)
            )
            BEGIN
                if ( SELECT EXISTS (SELECT 1 FROM users WHERE u_name = p_name OR u_email = p_email LIMIT 1) ) THEN
                    SELECT 'Username Exists !!';
                ELSE
                    INSERT INTO users
                    (
                        u_email,
                        u_name,
                        u_pass
                    )
                    VALUES
                    (
                        p_email,
                        p_name,
                        p_pass
                    );
                END IF;
            END
        """)
        cursor.execute(f"""
            CREATE DEFINER='{self.__user}'@'{self.__host}' PROCEDURE IF NOT EXISTS newdetl(
                IN p_name VARCHAR(20),
                IN p_count INT,
                IN p_coast INT
            )
            BEGIN
                if ( SELECT EXISTS (SELECT 1 FROM detali WHERE p_name = d_name LIMIT 1) ) THEN
                    SELECT 'Detal Exists !!';
                ELSE
                    INSERT INTO detali
                    (
                        d_name,
                        d_count,
                        d_coast
                    )
                    VALUES
                    (
                        p_name,
                        p_count,
                        p_coast
                    );
                END IF;
            END
        """) # ? Спросить у Ярика может сделать не ошибку а изменение
        cursor.execute(f"""
            CREATE DEFINER='{self.__user}'@'{self.__host}' PROCEDURE IF NOT EXISTS add_tehno_park(
                IN pt_name VARCHAR(100),
                IN p_description TEXT,
                IN p_moto_hours INT,
                IN p_fuil TINYINT,
                IN ps_name VARCHAR(100),
                IN images TEXT
            )
            BEGIN
                if ( SELECT EXISTS (SELECT 1 FROM tehno_park WHERE pt_name = t_name LIMIT 1) ) THEN
                    SELECT 'Tehno name Exists !!';
                ELSE
                    INSERT INTO tehno_park
                    (
                        t_name,
                        description,
                        moto_hours,
                        fuil,
                        status_id
                    )
                    VALUES
                    (
                        pt_name,
                        p_description,
                        p_moto_hours,
                        p_fuil,
                        (SELECT id FROM statuses WHERE ps_name = s_name LIMIT 1)
                    );
                END IF;
            END
        """)    # * Придумать спец символ и бить по нему строки или сделать цикл
        #-------------------------
    def create_triggers(self, cursor: CMySQLCursor):
        #---Создание триггеров----
        cursor.execute(f"""
            CREATE DEFINER='{self.__user}'@'{self.__host}' TRIGGER IF NOT EXISTS detal_trigger BEFORE INSERT ON detali_tehno
            FOR EACH ROW
            BEGIN
                UPDATE detali set detali.d_count = detali.d_count - NEW.d_count WHERE detali.id = NEW.d_id LIMIT 1;
            END
        """)
        #-------------------------
    def add_constant(self, cursor: CMySQLCursor):
        #------------------Заполнение таблиц-констант------------------
        cursor.execute("INSERT INTO t_satuses VALUES %s", (("broken", ), ("need service", ), ("on service", ), ("ready", ))) #TODO Добавить заполнение статусов
        cursor.execute("INSERT INTO m_statuses VALUES %s", (("firstcontact", ),  ("spam", ), ("irrelovant", ), ("waiting", ), ("complit deal", ), ("cross sale", )))
        cursor.execute("INSERT INTO m_statuses VALUES %s", (("1", ), ("2", )))
        cursor.execute("INSERT INTO types VALUES %s", (("Ремонт ДВС", ), ("Ремонт ходової частини", ), ("Ремонт електроніки", ), ("Обслуговування", ), ("Кузовні роботи", ), ("Ремонт підвіски", ), ("Ремонт гальм", ), ("Ремонт КПП", ), ("Шино монтаж", )))
        cursor.execute("INSERT INTO roles VALUES %s", (("Механік", ), ("Адмін", ), ("Продавець", ), ("Інструктор", )))
        #--------------------------------------------------------------


class DbMethods:
    """
    Class of methods to work with connection
    -------------------------------
    """
    def __init__(
        self, 
        сonn_obj: GetConnection
    ) -> None:
        self.__conn_obj = сonn_obj
    
    def __get_cursor(function_to_decorate) -> CMySQLCursor:
        """
        Wrapper to get cursor
        ---------------------
        * Using only in class DbMethods
        """
        def the_wrapper(
            self: DbMethods, 
            cursor: CMySQLCursor | None = None
        ) -> None:
            with self.__conn_obj.connection.cursor() as cursor:
                return function_to_decorate(self, cursor)
        return the_wrapper

    @__get_cursor
    def create_db(self, cursor: CMySQLCursor) -> None:
        """
        Method to create tables, procedures and triggers
        --------------------
        * Дальнейшие измененя написанны коментариями ниже в коде
        """
        self.__conn_obj.create_tables(cursor)
        self.__conn_obj.create_procedurc(cursor)
        self.__conn_obj.create_triggers(cursor)
        self.__conn_obj.add_constant(cursor)

    @__get_cursor
    def add_newdetal(
        self,
        cursor: CMySQLCursor,
        p_name: str,
        p_count: int,
        p_coast: int,
    ) -> bool:
        """
        Method to add new detal
        """
        cursor.callproc("add_newdetl", (p_name, p_count, p_coast))
        data = cursor.fetchall()
        if data: return False
        self.__conn_obj.connection.commit()
        return True
    
    @__get_cursor
    def add_techno_park(
        self,
        cursor: CMySQLCursor,
        pt_name: str,
        p_description: str,
        p_moto_hours: int,
        p_fuil: int,
        ps_name: str,
        images: list[str] | str    #TODO Определиться как поулчать картинки строчкой или списком строчек
    ) -> bool:
        """
        Method to add new car
        ---------------------
        """
        cursor.callproc("add_tehno_park", (pt_name, p_description, p_moto_hours, p_fuil, ps_name, images))
        data = cursor.fetchall()
        if data: return False
        self.__conn_obj.connection.commit()
        return True

    @__get_cursor
    def regestration(
        self,
        cursor: CMySQLCursor,
        u_email: str, 
        u_name: str, 
        u_pass: str
    ) -> bool:
        """
        Method to registration user
        --------------------
        """
        u_pass = generate_password_hash(password=u_pass, salt_length=54)
        cursor.callproc('user_registration',(u_email, u_name, u_pass))
        data = cursor.fetchall()
        data = cursor.fetchall()
        if data: return False
        self.__conn_obj.connection.commit()
        return True
    
    @__get_cursor
    def add_task(
        self,
        cursor: CMySQLCursor,
        user: str,
        fullname: str,
        phone: str,
        status: str, #? Спросить мб добавлять автоматически
        description: str
    ) -> bool:
        """
        Method to add new member
        ------------------------
        """
        cursor.callproc("add_task", (user, fullname, phone, status, description))
        data = cursor.fetchall()
        if data: return False
        self.__conn_obj.connection.commit()
        return True

    @__get_cursor
    def add_member(
        self,
        cursor: CMySQLCursor,
        user: str,
        fullname: str,
        phone: str,
        status: str, #? Спросить мб добавлять автоматически
        description: str
    ) -> bool:
        """
        Method to add new member
        ------------------------
        """
        cursor.callproc("add_member", (user, fullname, phone, status, description))
        data = cursor.fetchall()
        if data: return False
        self.__conn_obj.connection.commit()
        return True
    
    @__get_cursor
    def add_deal_action(
        self,
        cursor: CMySQLCursor,
        deal_id: int,
        description: str,
        task_id: int | None,
        status: str
    ) -> bool:
        """
        Method to add deal action
        -------------------------
        """
        cursor.callproc("add_deal_action", (deal_id, description, task_id, status))
        data = cursor.fetchall()
        if data: return False
        self.__conn_obj.connection.commit()
        return True

    @__get_cursor
    def login(
        self,
        cursor: CMySQLCursor,
        log: str, # * email | login
        password: str
    ) -> int | bool:
        """
        Method to login user
        --------------------
        """
        cursor.execute("""SELECT id, u_pass FROM users WHERE u_name = %s OR u_email = %s LIMIT 1""", (log, log)) #TODO Убрать кастыль с задвоением (log, log)
        result: tuple | None = cursor.fetchone()
        if not result: return False
        if not check_password_hash(result[1], password): return False
        session["userLogged"] = result[0]
        return result[0]
        
    @__get_cursor
    def get_info(
        self, 
        cursor: CMySQLCursor, 
        u_id: int | str
    ) -> tuple | bool:
        """
        Method to get user's info
        -------------------------
        """
        cursor.execute("SELECT * FROM users WHERE id = %s LIMIT 1", (u_id, ))
        result: tuple | None = cursor.fetchone()
        if not result: return False
        return result
        
    @__get_cursor
    def get_tables(
        self, 
        cursor: CMySQLCursor
    ) -> tuple | bool:
        """
        Method to get tables
        --------------------
        """
        cursor.execute("SHOW TABLES")
        data: list[tuple[str]] = cursor.fetchall()
        if not data: return False
        return tuple(i[0] for i in data) # * посмотреть можно ли обойтись без генератора
    
    @__get_cursor
    def get_table_info(
        self, 
        cursor: CMySQLCursor, 
        table: str
    ) -> tuple | bool:
        """
        Method to get info from table
        -----------------------------
        """
        cursor.execute(f"SELECT * FROM {table}")
        data: tuple | None = cursor.fetchall()
        if not data: return False
        return data
            

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
