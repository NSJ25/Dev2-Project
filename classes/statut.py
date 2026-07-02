from pathlib import Path
from sqlite3 import connect

class Statuts:

    def __init__(self):
        """Initialise la connexion à la base de données et le curseur SQLite."""
        self.__db_path = Path("..") / "database.db"
        self.__conn = connect(self.__db_path)
        self.__cursor = self.__conn.cursor()

    def create_statut(self, name):
        self.__cursor.execute(
            "INSERT INTO Status (statut) VALEUS (?)",
            (name,)
        )
        self.__conn.commit()

    def update_statut(self, statut_id, new_name):
        self.__cursor.execute(
            "UPDATE Statuts SET statut = ? WHERE id = ?",
            (new_name, statut_id)
        )
        self.__conn.commit()

    def delete_statut(self, name):
        self.__cursor.execute(
            "DELETE FROM Status WHERE statut = ?",
            (name,)
        )
        self.__conn.commit()

    def get_statut(self):
        pass

    def get_statut_id(self):
        pass

    if __name__ == "__main__":
        pass