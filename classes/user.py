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
        pass


    def change_password(self, name:str, password:str, naw_password:str):
        pass


    def get_user_id(self, name:str):
        pass


    def get_users(self):
        pass


    def delete_user(self, ident:int, name:str, password:str):
        pass


    def check(self,name:str, password:str):
        self.execute(
            "SELECT password FROM Users WHERE username = ?",
            (name,)
        )
        result = self.fetchone()
        if result is not None:
            return checkpw(password.encode("utf-8"), result[0].encode("utf-8"))
        else:
            return False


    if __name__ == "__main__":
        pass
