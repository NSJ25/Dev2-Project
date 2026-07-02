from pathlib import Path
from sqlite3 import connect

class Sujets:
    def __init__(self):
        self.__db_path = Path("..") / "database.db"
        self.__conn = connect(self.__db_path)
        self.__cursor = self.__conn.cursor()

    def create_sujet(self, name):
        """

        :param name:str
        :return:None
        """
        self.__cursor.execute(
            "INSERT INTO Sujets (sujet) VALUES (?)",
            (name,)
        )
        self.__conn.commit()

    def update_sujet(self, sujet_id, new_name):
        """

        :param sujet_id:int
        :param new_name:str
        :return:None
        """
        self.__cursor.execute(
            "UPDATE Sujets SET sujet = ? WHERE id = ?",
            (new_name, sujet_id)
        )
        self.__conn.commit()

    def delete_sujet(self, name):
        self.__cursor.execute(
            "DELETE FROM Sujets WHERE sujet = ?",
            (name,)
        )
        self.__conn.commit()

    

    def __name__(self):
        pass
