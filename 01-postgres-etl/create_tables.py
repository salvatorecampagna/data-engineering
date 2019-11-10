import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    '''
    Create the database and return a connection and cursor for querying it.
    Parameters:
        nothing
    Returns:
        cur: database cursor object
        conn: database connection object
    '''
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb \
        user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb \
        WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()

    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb \
        user=student password=student")
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    '''
    Drop database tables using the 'drop_table_queries'.
    Parameters:
        cur: database cursor object
        conn: database connection object
    Returns:
        nothing
    '''
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    '''
    Create database tables using the 'create_table_queries'.
    Parameters:
        cur: database cursor object
        conn: database connection object
    Returns:
        nothing
    '''
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    '''
    Database configuration entrypoint.
    Parameters:
        nothing
    Returns:
        nothing
    '''
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
