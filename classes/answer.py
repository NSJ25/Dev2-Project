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


    def edit_text(self, ident:int, text:str):
        self.execute(
        "UPDATE Answers SET answers_text = ? WHERE id = ?",
    (text, ident)
        )
        self.commit()


    def edit_is_correct(self, ident:int, boolean:bool):
        self.execute(
        "UPDATE Answers SET is_correct = ? WHERE id = ?",
            (boolean, ident)
        )
        self.commit()


    def edit_explanation(self, ident:int, txt:str):
        self.execute(
            "UPDATE Answers SET explanation = ? WHERE id = ?",
            (txt, ident)
        )
        self.commit()


    def delete_answer(self, ident:int):
        self.execute(
        "DELETE FROM Answers WHERE id = ?",
    (ident,)
        )
        self.commit()


    def get_answers_by_question(self, question_id:int):
        self.execute(
        "SELECT id, answers_text, is_correct, explanation FROM Answers WHERE question_id = ?",
    (question_id,)
        )
        return self.fetchall()



    if __name__ == "__main__":
        pass