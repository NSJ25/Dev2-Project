from classes.database_manager import DatabaseManager
from bcrypt import hashpw, gensalt, checkpw


class User(DatabaseManager):
    def __init__(self):
        super().__init__()


    def add_user(self, name:str, passwd:str):
        passwd = hashpw(passwd)
        pass


    def change_username(self, name:str, new_name:str, passwd:str):
        pass


    def change_password(self, name:str, passwd:str, naw_passwd:str):
        pass
    

    def get_user_id(self, name:str):
        pass


    def get_users(self):
        pass


    def delete_user(self, ident:int, name:str, passwd:str):
        pass


    def check(self, name:str, passwd:str):
        pass


    if __name__ == "__main__":
        pass




