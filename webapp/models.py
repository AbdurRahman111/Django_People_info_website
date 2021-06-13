from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
import hashlib
# Create your models here.
import uuid

class EmailConfirmed(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    activation_key=models.CharField(max_length=500)
    email_confirmed=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural='User Email-Confirmed'

@receiver(post_save, sender=User)
def create_user_email_confirmation(sender, instance, created, **kwargs):
    if created:
        dt=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        email_confirmed_instance=EmailConfirmed(user=instance)
        user_encoded=f'{instance.email}-{dt}'.encode()
        activation_key=hashlib.sha224(user_encoded).hexdigest()
        email_confirmed_instance.activation_key=activation_key
        email_confirmed_instance.save()


class person_information(models.Model):
    class Meta:
        verbose_name_plural = 'Person Information'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/Profile_image', null=True, blank=True, default='')
    First_name = models.CharField(max_length=500)
    Last_name = models.CharField(max_length=500)
    Other_name = models.CharField(max_length=500)
    State_of_Origin = models.CharField(max_length=500)
    Sex_Status = (('Male', "Male"),
              ('Female', "Female"),
              ('Other', "Other"))
    Sex = models.CharField(max_length=100, choices=Sex_Status, default="Progressing")
    Spoken_languages = models.CharField(max_length=500)
    Complexion_Status = (('Dark', "Dark"),
                  ('Chocolate', "Chocolate"),
                  ('Bleached', "Bleached"),
                  ('Light', "Light"))
    Complexion = models.CharField(max_length=100, choices=Complexion_Status, default="Progressing")
    Description = models.TextField()
    Adding_Time=models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return self.First_name



class contact_table(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Us'
    name=models.CharField(max_length=1000)
    email=models.CharField(max_length=1000)
    message=models.TextField()

    def __str__(self):
        return self.name
