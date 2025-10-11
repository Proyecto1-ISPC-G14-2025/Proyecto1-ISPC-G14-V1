import mysql.connector

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None
        
    def connect(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='farmastock'
        )
        self.cursor = self.conn.cursor(dictionary=True, buffered=True)
    
    def execute(self, query, params=None):
        self.cursor.execute(query, params)
    
    def fetchone(self):
        return self.cursor.fetchone()
    
    def commit(self):
        if self.conn:
            self.conn.commit()
    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            
    def fetchall(self):
     return self.cursor.fetchall()

    def commit(self):
      if self.conn:
        self.conn.commit()
        
