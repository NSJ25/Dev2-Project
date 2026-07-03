from classes.database_manager import DatabaseManager


class Question(DatabaseManager):
    def __init__(self):
        super.__init__()

    def add_question(self, text:str, subject_id:int, status_id:int, image:str=None):
        self.execute(
            "INSERT INTO Questions (text, subject_id, status_id, image_path) VALUES (?, ?, ?, ?, ?)",
            (text, subject_id, status_id, image)
        )
        self.commit()


    def edit_text(self, ident:int, new_text:str):
        self.execute(
            "UPDATE Qusetions SET text = ? WHERE id = ?",
            (new_text, ident)
        )
        self.commit()


    def edit_subject(self, ident:int, subject_id:str):
        self.execute(
            "UPDATE Qusetions SET subject_id = ? WHERE id = ?",
            (subject_id, ident)
        )
        self.commit()


    def edit_status(self, ident:int, status_id:str):
        self.execute(
            "UPDATE Qusetions SET status_id = ? WHERE id = ?",
            (status_id, ident)
        )
        self.commit()


    def edit_image(self, ident:int, new_path:str):
        self.execute(
            "UPDATE Qusetions SET image_path = ? WHERE id = ?",
            (new_path, ident)
        )
        self.commit()


    def remove_question(self, ident:int):
        self.execute(
            "DELETE FROM Questions WHERE id = ?",
            (ident,)
        )
        self.commit()


    def get_questions(self):
        pass


    def get_question_id(self):
        pass


    def get_questions_subject(self):
        pass


    def get_questions_sub_stat(self):
        pass


    if __name__ == "__main__":
        pass