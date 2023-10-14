import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)

crs = mydb.cursor()

execsqlcmd = lambda cmd, crs : crs.execute(cmd)
execcreatetable = lambda table, attrs, crs : execsqlcmd(f"CREATE TABLE {table} ({attrs});", crs)
execcreatedatabase = lambda dbname, crs : execsqlcmd(f"CREATE DATABASE {dbname};", crs)
execdropdatabase = lambda dbname, crs : execsqlcmd(f"DROP DATABASE {dbname};", crs)
execdroptable = lambda table, crs : execsqlcmd(f"DROP TABLE {table};", crs)
execusedatabase = lambda dbname, crs : execsqlcmd(f"USE {dbname};", crs)
execselectfromwhere = lambda attrs, table, wherecond, crs : execsqlcmd(f"SELECT {attrs} FROM {table} WHERE {wherecond};", crs)
execinsertinto = lambda table, attrs, values, crs : execsqlcmd(f"INSERT INTO {table} ({attrs}) VALUES ({values});", crs)

execcreatedatabase("mydatabase", crs)

execusedatabase("mydatabase", crs)

execcreatetable("USUARIOS", "id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), console VARCHAR(255)", crs)

execcreatetable("JOGOS", "id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), data_lancamento DATE", crs)

execinsertinto("USUARIOS", "nome, console", "'Thiago', 'PS2'", crs)

execinsertinto("JOGOS", "nome, data_lancamento", "'Cyberpunk 2077', '2020-12-10'", crs)

execselectfromwhere("*", "USUARIOS", "true", crs)

execselectfromwhere("*", "JOGOS", "true", crs)

execdroptable("USUARIOS", crs)

execdroptable("JOGOS", crs)

execdropdatabase("mydatabase", crs)

crs.close()
mydb.close()
