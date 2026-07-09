from classes.user import User

class Session:
    def __init__(self):
        self._user_manager = User()
        self._current_user = None
        self._connected = False

    def login(self, username, password):
        if self._connected:
            self.logout()

        if self._user_manager.check(username, password):
            self._connected = True
            self._current_user = username
            return "Succesful connection"
        return "Unsuccesful connection"

    def logout(self):
        self._current_user = None
        self._connected = False


    @property
    def is_connected(self):
        return self._connected

    @property
    def current_user(self):
        return self._current_user

