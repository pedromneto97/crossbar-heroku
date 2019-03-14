from mongoengine import *
import hashlib


class User(Document):
    username = StringField(required=True, unique=True)
    name = StringField(required=True)
    password = StringField(required=True)
    cpf = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)

    def save(self):
        self.password = self.encrypt(self.password, self.username)
        super().save()

    @staticmethod
    def encrypt(password: str, salt: str = None) -> str:
        a = hashlib.sha1()
        b = hashlib.sha1()
        a.update(password.encode('utf-8'))
        aux = ''
        if salt is not None:
            aux = salt
        b.update((str(a.hexdigest()) + aux).encode('utf-8'))
        return str(b.hexdigest())