from django.db import models

# Create your models here.
# MODEL은 데이터를 관리하는 부분


class Members(models.Model):
    user_id = models.CharField(max_length=30)
    pw = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=13)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]