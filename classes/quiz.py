from classes.answer import Answer
from classes.question import Question
from random import sample, shuffle




class Quiz:
    def __init__(self):
        self._quiz = []
        self._current_question = 0
        self._score = 0
        self._user_answers = []
        self._finished = False
        self._question = Question()
        self._answer = Answer()


    def create_quiz(self, subject_id):
        self._quiz.clear()
        self._current_question = 0
        self._score = 0
        self._user_answers.clear()
        self._finished = False

        q_fragile = [] # status fragile
        q_en_cours =[] # status en cours
        q_acquise = [] # status acquise

        self.prepare_question(q_fragile, self._question.get_questions_sub_stat(subject_id, 1))
        self.prepare_question(q_en_cours, self._question.get_questions_sub_stat(subject_id, 2))
        self.prepare_question(q_acquise, self._question.get_questions_sub_stat(subject_id, 3))

        self._quiz.extend(sample(q_fragile, 7))
        self._quiz.extend(sample(q_en_cours, 5))
        self._quiz.extend(sample(q_acquise, 3))

        shuffle(self._quiz)

    def prepare_question(self, table:list , data:list):
        for row in data:
            question={
                "id":row[0],
                "text":row[1],
                "subject":row[2],
                "status": row[3],
                "image":row[4]
                }
            table.append(question)








    if __name__ == "__main__":
        pass