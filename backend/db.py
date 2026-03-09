import psycopg2
from psycopg2.pool import SimpleConnectionPool
import os

class Database:
    def __init__(self):
        self.pool = None
    
    def init_app(self, app=None):
        self.pool = SimpleConnectionPool(
            1, 20,
            host=os.getenv('POSTGRES_HOST', 'localhost'),
            port=os.getenv('POSTGRES_PORT', 5432),
            database=os.getenv('POSTGRES_DB', 'fintech'),
            user=os.getenv('POSTGRES_USER', 'postgres'),
            password=os.getenv('POSTGRES_PASSWORD', 'password')
        )
    
    def get_connection(self):
        if not self.pool:
            raise Exception("Database not initialized")
        return self.pool.getconn()
    
    def return_connection(self, conn):
        if self.pool:
            self.pool.putconn(conn)

db = Database()
