import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

class Singleton(type):
    __instances = {}
    def __call__(cls, *args, **kwds):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwds)
        return cls.__instances[cls]

class DataBase(metaclass = Singleton):
    connection = None

    def connect(self):
        if self.connection is None:
            print("Nao existe conexao... criando conexao")
            self.connection = mysql.connector.connect(
                host = os.getenv('HOST'),
                database = os.getenv('DATABASE'),
                user = os.getenv('USER'),
                password = os.getenv('PASSWORD'),
            )
            self.cursor = self.connection.cursor()

        return self.cursor

    @staticmethod
    def _executar(query):
        connection = mysql.connector.connect(
                host = os.getenv('HOST'),
                database = os.getenv('DATABASE'),
                user = os.getenv('USER'),
                password = os.getenv('PASSWORD'),
            )
        cursor = connection.cursor()
        resultado = None

        try:
            cursor.execute(query)
            resultado = cursor.fetchall()
            connection.commit()
        except Exception as err:
            print(f'Erro na execução da query: {err}')
        
        cursor.close()
        connection.close()

        return resultado
    
if __name__ == '__main__':
    db1 = DataBase().connect()
    db2 = DataBase().connect()

    print(db1 is db2)