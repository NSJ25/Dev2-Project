from classes.user import User

class Session:
    """Gestion de la session utilisateur en mémoire.

    Utilise `User` pour la vérification des identifiants et conserve
    l'état de connexion courant (nom d'utilisateur et drapeau connecté).
    """
    def __init__(self):
        self._user_manager = User()
        self._current_user = None
        self._connected = False

    def login(self, username:str, password:str):
        """Tente de connecter un utilisateur.

        Si un utilisateur est déjà connecté, il est déconnecté avant la nouvelle tentative.

        Args:
            username (str): Nom d'utilisateur.
            password (str): Mot de passe en clair.

        Returns:
            str: Message indiquant le succès ou l'échec de la connexion.
        """
        if self._connected:
            self.logout()

        if self._user_manager.check(username, password):
            self._connected = True
            self._current_user = username
            return "Succesful connection"
        return "Unsuccesful connection"

    def logout(self):
        """Déconnecte l'utilisateur courant et réinitialise l'état."""
        if self._current_user is None:
            return "Aucun utilisateur n'est actuellement connecté."

        self._current_user = None
        self._connected = False

        return "Déconnexion réussie."


    @property
    def is_connected(self):
        """Retourne True si un utilisateur est connecté."""
        return self._connected

    @property
    def current_user(self):
        """Retourne le nom de l'utilisateur connecté ou None."""
        return self._current_user

if __name__ == "__main__":
    pass