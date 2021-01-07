import psycopg2

class db:
  def Init_db():
    conn = psycopg2.connect(dbname="ifood", user="postgres", password="docker", host="localhost", port=5435)
    return conn

  def Close_db(cur, conn):
    cur.close()
    conn.close()
