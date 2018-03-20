from django.db import models


class umm(models.Manager):
    def showall(self):
        return self.all()


class nmanager(models.Manager):
    def get(self):
        return super(nmanager, self).get_queryset().filter(username__contains='e')

class user(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    um = umm()
    fm = nmanager()
