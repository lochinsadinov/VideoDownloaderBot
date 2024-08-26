import psycopg2


class DB:
    con = psycopg2.connect(
        dbname='instagramtiktokdownloader',
        user='postgres',
        host='localhost',
        password='1',
        port=5432
    )

    cur = con.cursor()

    def insert(self):
        d = self.__dict__
        del d['cols']
        table_name = self.__class__.__name__.lower() + "s"
        keys = [k for k, v in d.items() if v is not None]
        col_names = " , ".join(keys)
        format = " , ".join(["%s"] * len(keys))
        params = [v for v in d.values() if v is not None]
        query = f"""
            insert into {table_name} ({col_names}) values ({format})
        """
        print(query)
        print(params)
        self.cur.execute(query, params)
        self.con.commit()

    def select(self, **conditions):
        table_name = self.__class__.__name__.lower() + "s"
        col_names = "*"
        conditions_format = ""
        if self.cols:
            col_names = " , ".join(self.cols)
        if conditions:
            conditions_format = " where " + " = %s and ".join(conditions.keys()) + " = %s"
        params = tuple(conditions.values())
        query = f"""
             select {col_names} from {table_name} {conditions_format}
        """
        self.cur.execute(query, params)
        return self.cur.fetchall()

    def delete(self, **conditions):
        table_name = self.__class__.__name__.lower() + "s"
        conditions_format = ""
        if conditions:
            conditions_format = " where " + " = %s and ".join(conditions.keys()) + " = %s"
        params = tuple(conditions.values())
        query = f"""
            delete from {table_name} {conditions_format}
        """
        self.cur.execute(query, params)
        self.con.commit()

    def update(self, **conditions):
        d = self.__dict__
        del d['cols']
        table_name = self.__class__.__name__.lower() + "s"
        keys = [k for k, v in d.items() if v is not None]
        values = [v for v in d.values() if v is not None]
        conditions_format = ""
        if conditions:
            conditions_format = " where " + " = %s and ".join(conditions.keys()) + " = %s"
        set_format = " = %s , ".join(keys) + "= %s"
        query = f"""
            update {table_name} set {set_format} {conditions_format}
        """
        params = tuple(values + list(conditions.values()))
        self.cur.execute(query, params)
        self.con.commit()


