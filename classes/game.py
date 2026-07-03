from classes.database_manager import DatabaseManager
from datetime import datetime

class Game(DatabaseManager):
    def __init__(self):
        super().__init__()

    def save_game(self, user_id,  score ):
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.execute(
            "INSERT INTO Games (user_id, date_game, score) VALUES (?, ?, ?) ",
            (user_id, date_now, score)
        )
        self.commit()

    def get_games_by_user(self, user_id):
        self.execute(
    """SELECT U.username, G.score, G.date_game 
            FROM Games AS G JOIN Users AS U ON G.user_id = U.id
            WHERE G.user_id = ?""",
    (user_id,)
        )
        return self.fetchall()


    def get_games_by_date(self, date_game):
        pass



    if __name__ == "__main__":
        pass