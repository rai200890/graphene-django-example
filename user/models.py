from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    last_name = models.CharField(max_length=200, db_index=True)
    email = models.EmailField(max_length=200, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)


class Phone(models.Model):
    ddd = models.CharField(max_length=2, db_index=True)
    number = models.CharField(max_length=9, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
