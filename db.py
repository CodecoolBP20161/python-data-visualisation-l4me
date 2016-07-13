import psycopg2



class Db():


    @staticmethod
    def execute_query(query):
        connect_str = "dbname='mate' user='postgres' host='localhost' password='alma'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data


#project = Db.execute_query("SELECT")