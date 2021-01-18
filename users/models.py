from django.db import models
from django.contrib.auth.models import AbstractUser
from conf.base import BaseModel


class User(AbstractUser, BaseModel):
    nick_name = models.CharField(max_length=20)


    class Meta:
        ordering = ("-created", )
        db_table = "users"
        verbose_name = "유저들"
        verbose_name_plural = "유저"

    def __str__(self):
        return self.username