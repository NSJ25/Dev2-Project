from pathlib import Path
import sqlite3

class DatabaseManager:
    def __int__(self):
        self.__db_path = Path("..") / "database.db"
        self.__conn = sqlite3.connect(self.__db_path)
        self.__cursor = self.__conn.cursor()

        


        