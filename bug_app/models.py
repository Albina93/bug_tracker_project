from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import  datetime, timezone 


class CustomUser(AbstractUser):
    bio = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class TicketModel(models.Model):
    STATUS_OF_TICKET_CHOICES = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        ('Invalid', 'Invalid'),
    ]
    title = models.CharField(max_length=90)
    submit_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=200)
    user_filed = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='user_filed')
    status = models.CharField(max_length=20, default='New', choices=STATUS_OF_TICKET_CHOICES)
    user_assigned = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_assigned', null=True)
    user_ticket_completed = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_ticket_completed', null=True)

    @property
    def age(self):
        date_submit = self.submit_time
        current_date = datetime.now(timezone.utc)
        age_day = current_date - date_submit
        return age_day.days



    def __str__(self):
        return self.title



