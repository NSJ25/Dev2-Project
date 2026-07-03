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

    def get_games_by_user(self, name):
        self.execute(
    """SELECT U.username, G.score, G.date_game 
            FROM Games AS G JOIN Users AS U ON G.user_id = U.id
            WHERE U.username = ? 
            ORDER BY G.date_game DESC""",
    (name,)
        )
        return self.fetchall()


    def get_games_by_date(self, date_game):
        date = datetime.strptime( date_game, "%d/%m/%Y").strftime("%Y-%m-%d")
        self.execute(
    """SELECT U.username, G.score, G.date_game 
            FROM Games AS G JOIN Users AS U ON G.user_id = U.id
            WHERE DATE(G.date_game) = ? 
            ORDER BY G.date_game DESC""",
    (date,)
        )
        return self.fetchall()


    if __name__ == "__main__":
        pass