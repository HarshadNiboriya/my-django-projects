from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length= 50)
    lastname = models.CharField(max_length= 50)
    loginid = models.CharField(max_length= 50)
    password = models.CharField(max_length= 50)
    address = models.CharField(max_length= 50)
    dob = models.CharField(max_length= 50)

    class Meta:
        db_table = 'sos_user'
