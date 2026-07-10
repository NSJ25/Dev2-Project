from classes.database_manager import DatabaseManager

class Status(DatabaseManager):
    """Gestion des statuts possibles pour une question.

    Fournit CRUD basique pour la table `Status`.
    """
    def __init__(self):
        super().__init__()
        pass

    def add_status(self, text:str):
        """Ajoute un nouveau statut.

        Args:
            text (str): Nom du statut.
        """
        self.execute(
            "INSERT INTO Status (name) VALUES (?)",
            (text,)
        )
        self.commit()

    def edit_status(self, ident:int, text:str):
        """Modifie le nom d'un statut.

        Args:
            ident (int): Identifiant du statut.
            text (str): Nouveau nom.
        """
        self.execute(
            "UPDATE Status SET name = ? WHERE id = ?",
            (text, ident)
        )
        self.commit()

    def remove_status(self, ident:int):
        """Supprime un statut par identifiant.

        Args:
            ident (int): Identifiant du statut.
        """
        self.execute(
            "DELETE FROM Status WHERE id = ?",
            (ident,)
        )
        self.commit()

    def get_status(self):
        """Retourne la liste des statuts (id, nom)."""
        self.execute(
            "SELECT id, name FROM Status"
        )
        return self.fetchall()

    def get_status_id(self, text:str):
        """Renvoie l'identifiant d'un statut à partir de son nom, ou -1."""
        self.execute(
            "SELECT id FROM Status WHERE name = ?",
            (text,)
        )
        result = self.fetchone()
        if result is not None:
            return result[0]
        return -1


    if __name__ == "__main__":
        pass