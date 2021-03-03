from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User, null=True, on_delete= models.CASCADE)
    username = models.CharField(max_length = 100, null = True)
    email = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.username

class Entry(models.Model):
    person  = models.ForeignKey(Person,null=True, on_delete= models.CASCADE)
    text = models.TextField(null=True)
    date_posted = models.DateTimeField(auto_now_add= True, null=True, blank=True)

    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'entries'    

