from textual.screen import Screen
from textual.widgets import Label, Button
from pyfiglet import Figlet


class QuizScreen(Screen):

    def compose(self):
        titre = Figlet(font="standard")
        yield Label(titre.renderText("Revision"))

        yield Label("Bienvenue sur la page de revision")

        yield Button("Menu", id="menu")

    def on_button_pressed(self, event):
        if event.button.id == "menu":
            self.app.push_screen("menu")


    if __name__ == "__main__":
        pass