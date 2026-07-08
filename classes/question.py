from classes.database_manager import DatabaseManager

class Question(DatabaseManager):
    def __init__(self):
        super().__init__()

    def add_question(self, text:str, subject_id:int, status_id:int, image:str=""):
        self.execute(
            "INSERT INTO Questions (text, subject_id, status_id, image_path) VALUES (?, ?, ?, ?)",
            (text, subject_id, status_id, image)
        )
        self.commit()


    def edit_text(self, ident:int, new_text:str):
        self.execute(
            "UPDATE Questions SET text = ? WHERE id = ?",
            (new_text, ident)
        )
        self.commit()


    def edit_subject(self, ident:int, subject_id:int):
        self.execute(
            "UPDATE Questions SET subject_id = ? WHERE id = ?",
            (subject_id, ident)
        )
        self.commit()


    def edit_status(self, ident:int, status_id:int):
        self.execute(
            "UPDATE Questions SET status_id = ? WHERE id = ?",
            (status_id, ident)
        )
        self.commit()


    def edit_image(self, ident:int, new_path:str):
        self.execute(
            "UPDATE Questions SET image_path = ? WHERE id = ?",
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
        self.execute(
        """ SELECT Q.id, Q.text, S.name, ST.name, Q.image_path
            FROM Questions AS Q 
                JOIN Subjects AS S ON Q.subject_id = S.id
                JOIN Status AS ST ON Q.status_id = ST.id
        """)
        return self.fetchall()


    def get_question_id(self, text:str):
        self.execute(
            "SELECT id FROM Questions WHERE text = ?",
            (text,)
        )
        result = self.fetchone()
        if result is not None:
            return result[0]
        else:
            return -1


    def get_questions_subject(self, subject_id:int):
        self.execute(
    """ SELECT Q.id, Q.text, S.name, ST.name, Q.image_path
            FROM Questions AS Q 
                JOIN Subjects AS S ON Q.subject_id = S.id
                JOIN Status AS ST ON Q.status_id = ST.id
            WHERE S.id = ? 
        """,
        (subject_id,)
        )
        return self.fetchall()



    def get_questions_sub_stat(self, subject_id:int, status_id:int):
        self.execute(
    """ SELECT Q.id, Q.text, S.name, ST.name, Q.image_path
            FROM Questions AS Q 
                JOIN Subjects AS S ON Q.subject_id = S.id
                JOIN Status AS ST ON Q.status_id = ST.id
            WHERE S.id = ? AND ST.id = ?
        """,
        (subject_id, status_id))
        return self.fetchall()


    if __name__ == "__main__":
        pass