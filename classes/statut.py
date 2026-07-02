from pathlib import Path
from sqlite3 import connect

class Statut:
    """Gestionnaire des statuts pour la base de données SQLite.

    Cette classe fournit des opérations CRUD sur la table `Status` ou `Statuts`.
    """

    def __init__(self):
        """Initialise la connexion à la base de données et le curseur SQLite."""
        self.__db_path = Path("..") / "database.db"
        self.__conn = connect(self.__db_path)
        self.__cursor = self.__conn.cursor()

    def create_statut(self, name):
        """Ajoute un nouveau statut en base de données.

        Args:
            name (str): Le texte du statut à insérer.

        Returns:
            None
        """
        self.__cursor.execute(
            "INSERT INTO Status (statut) VALEUS (?)",
            (name,)
        )
        self.__conn.commit()

    def update_statut(self, statut_id, new_name):
        """Met à jour le nom d'un statut existant.

        Args:
            statut_id (int): L'identifiant du statut à modifier.
            new_name (str): Le nouveau texte du statut.

        Returns:
            None
        """
        self.__cursor.execute(
            "UPDATE Statuts SET statut = ? WHERE id = ?",
            (new_name, statut_id)
        )
        self.__conn.commit()

    def delete_statut(self, name):
        """Supprime un statut en fonction de son nom.

        Args:
            name (str): Le texte du statut à supprimer.

        Returns:
            None
        """
        self.__cursor.execute(
            "DELETE FROM Status WHERE statut = ?",
            (name,)
        )
        self.__conn.commit()

    def get_statuts(self):
        """Récupère tous les statuts stockés en base de données.

        Returns:
            list[tuple[int, str]]: Liste des tuples contenant l'ID et le statut.
        """
        self.__cursor.execute(
            "SELECT id, statut FROM Statuts"
        )
        return self.__cursor.fetchall()

    def get_statut_id(self, name):
        """Récupère l'identifiant d'un statut à partir de son texte.

        Args:
            name (str): Le texte du statut à rechercher.

        Returns:
            list[tuple[int]]: Liste des tuples contenant l'ID trouvé.
        """
        self.__cursor.execute(
            "SELECT id FROM Statuts WHERE statut = ?",
            (name,)
        )
        self.__conn.commit()
        return self.__cursor.fetchall()

    if __name__ == "__main__":
        pass