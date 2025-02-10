import bcrypt

from infrastracture.adapters.alert_adapter import AlertsAdapter
from application.repositories.alert_repository import AlertsRepository
from application.repositories.crypto_repository import CryptocurrencyRepository
from tools import generate_unique_id


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)


class User:
    def __init__(self,  username, password_hash):
        self.username = username
        self.password_hash = password_hash

        self.crypto_storage = CryptocurrencyRepository()
        self.alert_storage = AlertsRepository(self.crypto_storage) # ! Only here where we link crypto_storage whith AlertsRepository
        self.alert_adapter = AlertsAdapter(self.alert_storage)



class UserRegistry:
    def __init__(self):
        self.users = {}

    def checking_for_user(self, username):
        if username in self.users:
            return True
        return False

    def register_new_user(self,  username, password):
        password_hash = hash_password(password)
        new_user = User(username, password_hash)

        self.users[username] = new_user
        return self.users[username]

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if check_password(password, user.password_hash):
            return user
        else:
            return False

    def delete_user(self, username):
        del self.users[username]
