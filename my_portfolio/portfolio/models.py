from django.db import models

# Create your models here.
class visitor_note(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mob_number = models.CharField(max_length=20)
    email_subject = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
