from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Group(models.Model):
    title = models.CharField(max_length=100, default="new-group")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    datecreated = models.DateField()
    details = models.TextField(null=True, blank=True)
    image = models.ImageField(null = True, blank = True, upload_to = 'images/')

    def __str__(self):
        return f'{self.title} by {self.owner}'

class GroupMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} in {self.group}'

class Purchase(models.Model):
    spender = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    amount = models.FloatField(default= 0.0)
    details = models.TextField(null=True, blank=True)
    datecreated = models.DateField()
    topic = models.CharField(max_length=60, null = True, blank=True)
    status = models.CharField(max_length=60, default="Pending")
    
    def __str__(self):
        return f'{self.spender} in {self.group} of {self.amount}'


class Transaction(models.Model):
    spender = models.ForeignKey(User, on_delete = models.CASCADE, related_name="expenses")
    amount = models.FloatField(default= 0.0)
    getter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="backexpenses")
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100, null = True, blank=True)
    
    def __str__(self):
        return f'{self.spender} to {self.getter}'

class ProfilePicture(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    picture = models.ImageField(null = True, blank = True, upload_to = 'images/')

    def __str__(self):
        return f'{self.user} image'