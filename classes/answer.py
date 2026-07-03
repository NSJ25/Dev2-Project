from classes.database_manager import DatabaseManager


class Answer(DatabaseManager):
    def __init__(self):
        super().__init__()


    def add_answer(self, question_id:int, text:str, is_correct:bool=False, explanation:str=""):
        self.execute(
        "INSERT INTO Answers (question_id, answers_text, is_correct, explanation) VALUES (?, ?, ?, ?)",
    (question_id, text, is_correct, explanation)
        )
        self.commit()


    def edit_text(self, ident, text):
        self.execute(
        "UPDATE Answers SET answers_text = ? WHERE id = ?",
    (text, ident)
        )
        self.commit()


    def edit_is_correct(self, ident, boolean):
        self.execute(
        "UPDATE Answers SET is_correct = ? WHERE id = ?",
            (boolean, ident)
        )
        self.commit()


    def edit_explanation(self, ident, txt):
        self.execute(
            "UPDATE Answers SET explanation = ? WHERE id = ?",
            (txt, ident)
        )
        self.commit()


    def delete_answer(self, ident):
        self.execute(
        "DELETE FROM Answers WHERE id = ?",
    (ident,)
        )
        self.commit()


    def get_answers_by_qestion(self, question_id):
        pass



    if __name__ == "__main__":
        pass