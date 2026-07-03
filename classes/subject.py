from classes.database_manager import DatabaseManager

class Subject(DatabaseManager):
    def __init__(self):
        super().__init__()

    def add_subject(self, text:str):
        self.execute(
            "INSERT INTO Subjects (name) VALUES (?)",
            (text,)
        )
        self.commit()


    def edit_subject(self, ident:int, text:str):
        self.execute(
            "UPDATE Subjects SET name = ? WHERE id = ?",
            (text, ident)
        )
        self.commit()

    def remove_subject(self, ident:int):
        self.execute(
            "DELETE FROM Subjects WHERE id = ?",
            (ident,)
        )
        self.commit()


    def get_subjects(self):
        self.execute(
            "SELECT id, name FROM Subjects"
        )
        return self.fetchall()

    def get_subject_id(self, text:str):
        self.execute(
            "SELECT id FROM Subjects WHERE name = ?",
            (text,)
        )
        result = self.fetchone()
        if result is not None:
            return result[0]
        return -1

    if __name__ == "__main__":
        pass