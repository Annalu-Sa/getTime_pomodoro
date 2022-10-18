import sqlite3

conn = sqlite3.connect('get_Time.db')
c = conn.cursor()

c.execute('''
          CREATE TABLE login_get_Time
                (id INTEGER NOT NULL PRIMARY KEY, 
                email TEXT NOT NULL, 
                 senha TEXT NOT NULL 
          );
          ''') 
        
conn.comit()

