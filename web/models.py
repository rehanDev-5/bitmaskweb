from django.db import models
from django_quill.fields import QuillField

from django.core.mail import EmailMessage

from .thread import SendMailClass
from main import settings
# Create your models here.

CATEGORY = (
    ('IOT',"IOT"),
    ('FIRMWARE',"FIRMWARE"),
    ('WEBAPPS',"WEBAPPS"),
)

class UserQuery(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,null=True)
    pno = models.CharField(max_length=20)
    msg = models.CharField(max_length=1000)

    def notify_admin(self):
        message_u = f'Name: {self.name}\nEMail: {self.email}\nPno: {self.pno}\nMessage: {self.msg}'
        mail = EmailMessage("You Got New Query From Website!!", message_u, settings.EMAIL_HOST_USER, ['info@bitmasktech.com'])
        SendMailClass(mail).start()

    def save(self, *args, **kwargs):
        self.notify_admin()
        super(UserQuery, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.email}"

class Blog(models.Model):
    title = models.CharField(max_length=255,default='none')
    category = models.CharField(max_length=25,choices=CATEGORY,default='none')
    description = models.CharField(max_length=255,default='none')
    img = models.FileField(upload_to='blogs/',default='none')
    content = QuillField()

    def __str__(self) -> str:
        return self.title

class Comments(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    txt = models.CharField(max_length=255,default='none')
    name = models.CharField(max_length=255,default='none')

    def __str__(self) -> str:
        return self.txt