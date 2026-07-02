from pathlib import Path
from sqlite3 import connect


class DatabaseManager:
    def __init__(self):
        base_dir = Path(__file__).resolve().parent.parent
        self._db_path = base_dir / "database.db"
        self._conn = connect(self._db_path)
        self._cursor = self._conn.cursor()


    def execute(self, sql, params=()):
        self._cursor.execute(sql, params)


    def fetchone(self):
        return self._cursor.fetchone()


    def fetchall(self):
        return self._cursor.fetchall()


    def commit(self):
        self._conn.commit()


    def close(self):
        self._conn.close()

    if __name__ == "__main__":
        pass