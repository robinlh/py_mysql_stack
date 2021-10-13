from sqlalchemy import create_engine

# connection string components:
# connect to db as root user with password:"password" - root:password
# connect to mysql db host on standard port - @mysql:3306
# connect to database test - /test
mysql_conn_str = "mysql+pymysql://root:password@mysql:3306/test"
engine = create_engine(mysql_conn_str)
connection = engine.connect()
q = connection.execute('SHOW DATABASES')
available_tables = q.fetchall()
print(available_tables)