from django.contrib.auth.models import User
from django.db.models import CASCADE, DateTimeField, Model, OneToOneField


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    created = DateTimeField(auto_now_add=True)
