import sqlite3
from sqlite3 import Error


def update_task(conn, task):
    """
    update priority, begin_date, and end_date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = '''UPDATE tasks
            SET priority = ?,
            begin_date = ?,
            end_date = ?
            WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def main():
    database = "L:\\SeqPilot_2017\SQLite_NGS\db\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        update_task(conn, (2, '2018-02-23', '2018-02-28', 1))


if __name__ == '__main__':
    main()