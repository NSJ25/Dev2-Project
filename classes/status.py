from classes.database_manager import DatabaseManager


class Status(DatabaseManager):
    def __init__(self):
        super().__init__()
        pass

    def add_status(self, text):
        self.execute(
            "INSERT INTO Status (name) VALUES (?)",
            (text,)
        )
        self.commit()

    def edit_status(self,text, ident):
        self.execute(
            "UPDATE Status SET name = ? WHERE id = ?",
            (text, ident)
        )
        self.commit()

    def remove_status(self, ident):
        self.execute(
            "DELETE FROM Status WHERE id = ?",
            (ident,)
        )
        self.commit()

    def get_status(self):
        pass

    def get_status_id(self):
        pass


    if __name__ == "__main__":
        pass