import psycopg2
import psycopg2.extras as ext


def run_sql(sql, values=None):
    conn = None
    results = []

    try:
        conn = psycopg2.connect("passfile=.pgpass user=doadmin host=db-postgresql-lon1-07772-do-user-8246268-0.b.db.ondigitalocean.com port=25060 dbname=gym sslmode=require")
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results
