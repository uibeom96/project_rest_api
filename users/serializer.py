from rest_framework import serializers
from users.models import User


class User_Serializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "nick_name", "username", "email")
