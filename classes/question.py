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

    def edit_subject(self):
        pass

    def edit_status(self):
        pass

    def edit_image(self):
        pass

    def remove_question(self):
        pass

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