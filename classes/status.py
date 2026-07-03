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
        self.execute(
            "SELECT id, name FROM Status"
        )
        return self.fetchall()

    def get_status_id(self, text):
        self.execute(
            "SELECT id FROM Status WHERE name = ?",
            (text,)
        )
        result = self.fetchone()
        if result is not None:
            return result[0]
        else:
            return -1


    if __name__ == "__main__":
        pass