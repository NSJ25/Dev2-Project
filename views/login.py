import tkinter as tk
from classes.database_manager import DatabaseError
from classes.user import AuthenticationError, UserNotFoundError
import re


class LoginPage(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller)

        self.controller = controller


        # Zone 1
        self.top_frame = tk.Frame(self)
        self.top_frame.pack(
            fill="both",
            expand=True
        )


        # Zone 2
        self.center_frame = tk.Frame(self)
        self.center_frame.pack(
            fill="both",
            expand=True
        )


        # Zone 3
        self.form_frame = tk.Frame(self)
        self.form_frame.pack(
            fill="both",
            expand=True
        )


        # Zone 4
        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack(
            fill="both",
            expand=True
        )


        self.title = tk.Label(
            self.top_frame,
            text="Bienvenue sur la page de connexion",
            font=("Arial", 20)
        )
        self.title.pack(pady=20)


        btn_menu = tk.Button(
            self.center_frame,
            text="[ MENU ]",
            command=lambda:
            controller.show_page("MenuPage")
        )
        btn_menu.pack()


        self.info = tk.Label(
            self.bottom_frame,
            text=""
        )
        self.info.pack(pady=10)


        btn_login = tk.Button(
            self.center_frame,
            text="[ Se connecter ]",
            command = self.login_form
        )
        btn_login.pack()


        btn_logout = tk.Button(
            self.center_frame,
            text="[ Se deconnecter ]",
            command=self.logout
        )
        btn_logout.pack()


        btn_add_user = tk.Button(
            self.center_frame,
            text="[ Créer un utilisateur ]",
            command=self.create_user_form
        )
        btn_add_user.pack()


        btn_remove_user = tk.Button(
            self.center_frame,
            text="[ Supprimer un utilisateur ]",
            command=self.delete_user_form
        )
        btn_remove_user.pack()



    def show_message(self, message):
        self.info.config(
            text=str(message)
        )


    def clear_form(self):
        for widget in self.form_frame.winfo_children():
            widget.destroy()


    def login_form(self):
        self.clear_form()
        self.show_message("")

        tk.Label(self.form_frame, text="Nom d'utilisateur").pack()
        self.username = tk.Entry(self.form_frame)
        self.username.pack()

        tk.Label(self.form_frame, text="Mot de passe").pack()
        self.password = tk.Entry(self.form_frame, show="*")
        self.password.pack()

        tk.Button(
            self.form_frame,
            text="Valider",
            command= self.login
        ).pack()


    def login(self):

        username = self.username.get().strip()
        passwd = self.password.get().strip()

        if not re.match("^[a-zA-Z0-9]+$", username):
            self.show_message("Le nom d'utilisateur contient des caractères non autorisés")
            return

        try:

            msg = self.controller.session.login(username, passwd)
            self.show_message(msg)
            self.clear_form()

        except (DatabaseError, ValueError, TypeError) as e:
            self.show_message(e)
            print(e)
            return


    def logout(self):
        self.clear_form()
        self.show_message("")
        msg = self.controller.session.logout()
        self.show_message(msg)




    def create_user_form(self):
        self.clear_form()
        self.show_message("")

        tk.Label(self.form_frame, text="Nom d'utilisateur").pack()
        self.username = tk.Entry(self.form_frame)
        self.username.pack()

        tk.Label(self.form_frame, text="Mot de passe").pack()
        self.password = tk.Entry(self.form_frame, show="*")
        self.password.pack()

        tk.Button(
            self.form_frame,
            text="Valider",
            command=self.create_user
        ).pack()



    def create_user(self):
        username = self.username.get().strip()
        passwd = self.password.get().strip()

        if not re.match("^[a-zA-Z0-9]+$", username):
            self.show_message("Le nom d'utilisateur contient des caractères non autorisés")
            return

        try:

            self.controller.user.add_user(username, passwd)
            self.show_message("Utilisateur créé avec succès")
            self.clear_form()

        except (DatabaseError, AuthenticationError, UserNotFoundError, TypeError, ValueError) as e:
            self.show_message(e)
            print(str(e))
            return


    def delete_user_form(self):
        self.clear_form()
        self.show_message("")

        tk.Label(self.form_frame, text="Nom d'utilisateur").pack()
        self.username = tk.Entry(self.form_frame)
        self.username.pack()

        tk.Label(self.form_frame, text="Mot de passe").pack()
        self.password = tk.Entry(self.form_frame, show="*")
        self.password.pack()

        tk.Button(
            self.form_frame,
            text="Valider",
            command=self.delete_user
        ).pack()

    def delete_user(self):
        username = self.username.get().strip()
        passwd = self.password.get().strip()

        try:

            self.controller.user.delete_user(username, passwd)
            self.show_message("Utilisateur supprimé avec succès")
            self.clear_form()

        except (DatabaseError, AuthenticationError, UserNotFoundError, TypeError, ValueError) as e:
            self.show_message(e)
            print(str(e))
            return




