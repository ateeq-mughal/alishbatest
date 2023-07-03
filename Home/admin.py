from django.contrib import admin
from Home.models import Contact


# Register your models here.
admin.site.register(Contact) #after registering, we will be able to see the models in the admin panel of our website
