from django.shortcuts import render
from users.serializer import User_Serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import User


@api_view(["GET"])
def user_list(request):
    users = User.objects.all()
    serializer = User_Serializers(users, many=True)
    return Response(serializer.data)

