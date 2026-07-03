from classes.database_manager import DatabaseManager
from bcrypt import hashpw, gensalt, checkpw


class User(DatabaseManager):
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
        if self.check(name, password):
            passwd = hashpw(new_password.encode("utf-8"), gensalt()).decode("utf-8")
            self.execute(
            "UPDATE FROM Users SET password = ? WHERE namev = ?",
            (passwd, name)
            )
            self.commit()
            return f"Le mot de passe de l'utilisateur {name} à ete changer avec succès."
        else:
            return f"Nom d'utilisateur ou mot de passe incorrect."



    def get_user_id(self, name:str):
        self.execute(
        "SELECT id FROM Users WHERE username = ?",
        (name,)
        )
        result = self.fetchone()
        if result is not None:
            return result[0]
        return -1


    def get_users(self):
        self.execute(
            "SELECT id, username FROM Users"
        )
        return self.fetchall()


    def delete_user(self, name:str, password:str):
        if self.check(name, password):
            self.execute(
            "DELETE FROM Users WHERE usename = ?",
                (name,)
            )
            self.commit()
            return f"L'utilisateur {name} a été supprimé avec succès."
        else:
            return f"Nom d'utilisateur ou mot de passe incorrect."



    def check(self, name:str, password:str):
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
