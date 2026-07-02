from pathlib import Path
from sqlite3 import connect

class Sujet:
    """Gestionnaire des sujets pour la base de données SQLite.

    Cette classe fournit des opérations CRUD sur la table `Sujets`.
    """

    def __init__(self):
        """Initialise la connexion à la base de données et le curseur SQLite."""
        self.__db_path = Path("..") / "database.db"
        self.__conn = connect(self.__db_path)
        self.__cursor = self.__conn.cursor()

    def create_sujet(self, name):
        """Ajoute un nouveau sujet en base de données.

        Args:
            name (str): Le nom du sujet à insérer.

        Returns:
            None
        """
        self.__cursor.execute(
            "INSERT INTO Sujets (sujet) VALUES (?)",
            (name,)
        )
        self.__conn.commit()

    def update_sujet(self, sujet_id, new_name):
        """Met à jour le nom d'un sujet existant.

        Args:
            sujet_id (int): L'identifiant du sujet à modifier.
            new_name (str): Le nouveau nom du sujet.

        Returns:
            None
        """
        self.__cursor.execute(
            "UPDATE Sujets SET sujet = ? WHERE id = ?",
            (new_name, sujet_id)
        )
        self.__conn.commit()

    def delete_sujet(self, name):
        """Supprime un sujet en fonction de son nom.

        Args:
            name (str): Le nom du sujet à supprimer.

        Returns:
            None
        """
        self.__cursor.execute(
            "DELETE FROM Sujets WHERE sujet = ?",
            (name,)
        )
        self.__conn.commit()

    def get_sujets(self):
        """Récupère tous les sujets stockés en base de données.

        Returns:
            list[tuple[int, str]]: Liste des tuples contenant l'ID et le nom du sujet.
        """
        self.__cursor.execute(
            "SELECT id, sujet FROM Sujets"
        )
        return self.__cursor.fetchall()

    def get_sujet_id(self, name):
        """Récupère l'identifiant d'un sujet à partir de son nom.

        Args:
            name (str): Le nom du sujet à rechercher.

        Returns:
            list[tuple[int]]: Liste des tuples contenant l'ID trouvé.
        """
        self.__cursor.execute(
            "SELECT id FROM Sujets WHERE sujet = ?",
            (name,)
        )
        self.__conn.commit()
        return self.__cursor.fetchall()

    if __name__ == "__main__":
        pass
