from pathlib import Path
from sqlite3 import connect


class DatabaseManager:
    """Gestion basique de la connexion SQLite et méthodes utiles.

    Fournit une connexion au fichier `database.db` situé à la racine du projet
    et encapsule les opérations courantes sur le curseur.
    """

    def __init__(self):
        """Initialise la connexion et le curseur vers la base de données."""
        base_dir = Path(__file__).resolve().parent.parent
        self._db_path = base_dir / "database.db"
        self._conn = connect(self._db_path)
        self._cursor = self._conn.cursor()


    def execute(self, sql, params=()):
        """Exécute une requête SQL avec paramètres optionnels.

        Args:
            sql (str): Requête SQL à exécuter.
            params (tuple): Paramètres à passer à la requête.
        """
        self._cursor.execute(sql, params)


    def fetchone(self):
        """Récupère une seule ligne du résultat de la dernière requête."""
        return self._cursor.fetchone()


    def fetchall(self):
        """Récupère toutes les lignes du résultat de la dernière requête."""
        return self._cursor.fetchall()


    def commit(self):
        """Valide (commit) la transaction courante."""
        self._conn.commit()


    def close(self):
        """Ferme la connexion à la base de données."""
        self._conn.close()

if __name__ == "__main__":
    pass