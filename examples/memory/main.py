import libsql_experimental as libsql

conn = libsql.connect(":memory:")
cur = conn.cursor()

conn.execute("CREATE TABLE IF NOT EXISTS users (name TEXT);")
conn.execute("INSERT INTO users VALUES ('first@example.com');")
conn.execute("INSERT INTO users VALUES ('second@example.com');")
conn.execute("INSERT INTO users VALUES ('third@example.com');")


print(conn.execute("select * from users").fetchall())
