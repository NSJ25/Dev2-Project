from pathlib import Path
from sqlite3 import connect
from bcrypt import hashpw, gensalt, checkpw

class Utilisateur:
    def __init__(self):
        """Initialise la connexion à la base de données et le curseur SQLite."""
        self.__db_path = Path("..") / "database.db"
        self.__conn = connect(self.__db_path)
        self.__cursor = self.__conn.cursor()

    def create_user(self, nom, password):
        passwd = hashpw(password.encode("utf-8"),gensalt()).decode("utf-8")

        self.__cursor.execute(
            "INSERT INTO Utilisateurs (nom, password) VALUES ( ?, ?, )",
            (nom, passwd)
        )
        self.__conn.commit()

    def update_nom(self,pseudo, password, nom, prenom):
       pass

    def update_passwd(self, pseudo, password, new_password):
       pass

    def delete_user(self):
        pass

    def get_users(self):
        pass

    def get_user_id(self):
        pass

    if __name__ == "__main__":
        pass
