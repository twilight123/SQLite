import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None"""

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = '''INSERT INTO projects(name,begin_date,end_date)
            VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid


def create_task(conn, task):
    """Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = '''INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
            VALUES(?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid


def main():
    database = "L:\\SeqPilot_2017\SQLite_NGS\db\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        project = ('NGS database with SQLite and Python', '2018-02-22', '2018-03-22')
        project_id = create_project(conn, project)

        # tasks
        task_1 = ('Get database structure of NGS.db', 1, 1, project_id, '2018-02-22', '2018-02-28')
        task_2 = ('Confirm with user the structure', 1, 1, project_id, '2018-02-22', '2018-03-03')

        # create tasks
        create_task(conn, task_1)
        create_task(conn, task_2)


if __name__ == '__main__':
    main()
