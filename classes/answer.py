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


    def edit_text(self):
        self.execute()
        pass


    def edit_is_correct(self):
        pass


    def edit_explanation(self):
        pass


    def delete_answer(self):
        pass


    def get_answers_by_qestion(self):
        pass



    if __name__ == "__main__":
        pass