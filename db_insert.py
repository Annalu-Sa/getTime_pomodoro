import sqlite3

conn = sqlite3.connect('get_Time.db') 
c = conn.cursor()


c.execute('''
        INSERT INTO login_get_Time (id, email, senha) 
        VALUES (1, "buda@gmail.com", "buda123");
        
''')

c.execute('''
        INSERT INTO login_get_Time (id, email, senha) 
        VALUES (2, "giselly@gmail.com", "giselly123")

 ''')

c.execute('''
        INSERT INTO login_get_Time (id, email, senha) 
        VALUES (3, "kellypinheirosoares@poli.ufrj.br", "kelly123")

 ''')


                     
conn.commit()

print('Tabela criada com sucesso.')

conn.close()
