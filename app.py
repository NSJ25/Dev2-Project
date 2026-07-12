from classes.quiz import Quiz
from classes.session import Session
from classes.game import Game
from classes.user import User

from textual.app import App
from screens.menu import MenuScreen
from screens.login import LoginScreen
from screens.quiz import QuizScreen
from screens.setting import SettingScreen


class QuizApp(App):
    def __init__(self):
        super().__init__()
        self.session = Session()
        self.game = Game()
        self.quiz = Quiz()
        self.user = User()

    SCREENS = {
        "menu": MenuScreen,
        "login": LoginScreen,
        "setting": SettingScreen,
        "quiz" : QuizScreen
    }

    def on_mount(self):
        self.push_screen(MenuScreen())

    if __name__ == "__main__":
        pass