
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