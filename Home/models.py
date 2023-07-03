from django.db import models

# makemigrations mean create changes and store in a file
# migrate means apply the pending changes created by makemigrations; apply means write it in the database dbsqlite

class Contact(models.Model):
    name = models.CharField(max_length=120,unique=True)
    phone = models.CharField(max_length=12,null=True)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=20)
    desc = models.TextField(default='write description')
    date = models.DateField()

    def __str__(self): #technique to change the model and the contact entries will come as names of the users in admin
        return self.name
    
