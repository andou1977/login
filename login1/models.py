from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

        def __str__(self):
            return self.name

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Test, self).save(*args, **kwargs)


