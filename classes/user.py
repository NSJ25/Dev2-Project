from classes.database_manager import DatabaseManager
from bcrypt import hashpw, gensalt, checkpw


class User(DatabaseManager):
    """Gestion des opérations liées aux utilisateurs.

    Encapsule la création, modification, suppression et vérification
    des utilisateurs stockés dans la table `Users`.
    """
    def __init__(self):
        super().__init__()


    def add_user(self, name:str, password:str):
        passwd = hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")
        self.execute(
        "INSERT INTO Users (username, password) VALUES (?, ?)",
    (name, passwd)
        )
        self.commit()



    def change_username(self, name:str, new_name:str, password:str):
        if self.check(name, password):
            self.execute(
                "UPDATE Users SET username = ? WHERE username = ?",
                (new_name, name)
            )
            self.commit()
            return f"Le nom d'utilisateur {name} à ete changer en {new_name} avec succès."
        else:
            return f"Nom d'utilisateur ou mot de passe incorrect."


    def change_password(self, name:str, password:str, new_password:str):
        """Change le mot de passe d'un utilisateur après vérification.

        Args:
            name (str): Nom de l'utilisateur.
            password (str): Mot de passe actuel.
            new_password (str): Nouveau mot de passe.

        Returns:
            str: Message indiquant le résultat de l'opération.
        """
        if self.check(name, password):
            passwd = hashpw(new_password.encode("utf-8"), gensalt()).decode("utf-8")
            self.execute(
            "UPDATE Users SET password = ? WHERE username = ?",
            (passwd, name)
            )
            self.commit()
            return f"Le mot de passe de l'utilisateur {name} à ete changer avec succès."
        else:
            return f"Nom d'utilisateur ou mot de passe incorrect."



    def get_user_id(self, name:str):
        """Renvoie l'identifiant d'un utilisateur à partir de son nom, ou -1."""
        self.execute(
        "SELECT id FROM Users WHERE username = ?",
        (name,)
        )
        result = self.fetchone()
        if result is not None:
            return result[0]
        return -1


    def get_users(self):
        """Retourne la liste des utilisateurs (id, username)."""
        self.execute(
            "SELECT id, username FROM Users"
        )
        return self.fetchall()


    def delete_user(self, name:str, password:str):
        """Supprime un utilisateur après vérification du mot de passe.

        Args:
            name (str): Nom de l'utilisateur.
            password (str): Mot de passe pour authentifier la suppression.

        Returns:
            str: Message indiquant le résultat de l'opération.
        """
        if self.check(name, password):
            self.execute(
            "DELETE FROM Users WHERE username = ?",
                (name,)
            )
            self.commit()
            return f"L'utilisateur {name} a été supprimé avec succès."
        else:
            return f"Nom d'utilisateur ou mot de passe incorrect."


    def check(self, name:str, password:str):
        """Vérifie qu'un couple nom/mot de passe est valide.

        Returns:
            bool: True si les identifiants sont corrects, False sinon.
        """
        self.execute(
        "SELECT password FROM Users WHERE username = ?",
        (name,)
        )
        result = self.fetchone()
        if result is not None:
            return checkpw(password.encode("utf-8"), result[0].encode("utf-8"))
        return False


    if __name__ == "__main__":
        pass
