from textual.screen import Screen
from textual.widgets import Label, Button
from pyfiglet import Figlet



class MenuScreen(Screen):

    CSS = """

        Screen {
            background: black;
            color: green;
        }

        Label {
            color: green;
        }
        
        Button { 
            background: darkgreen;
            color: black;
        }

        """

    def compose(self):
        titre = Figlet(font="rev")
        yield Label(titre.renderText("Feu Vert"))

        yield Button("Connexion", id="login")
        yield Button("Revision", id="quiz")
        yield Button("Reglages", id="setting")

    def on_button_pressed(self, event):
        if event.button.id == "login":
            self.app.push_screen("login")

        elif event.button.id == "quiz":
            self.app.push_screen("quiz")

        elif event.button.id == "setting":
            self.app.push_screen("setting")






    if __name__ == "__main__":
        pass

