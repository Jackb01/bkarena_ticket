from django.db import models

class UserTbl(models.Model):
   
    pin = models.CharField("Personal Identification Number", unique=True, max_length=240)
    full_name = models.CharField("Full Name", max_length=240)
    email = models.EmailField("Email", unique=True)
    created = models.DateField("Created On", auto_now_add=True)

    def __str__(self):
        return self.pin


class TicketTbl(models.Model):

    EVENT_STATUS_CHOICES = (
        ('NORMAL', 'Normal'),
        ('VIP', 'VIP'),
        ('GOLD', 'Gold'),
    )

    user = models.ForeignKey(UserTbl, on_delete=models.CASCADE, null=False)
    event_name = models.CharField("Event Name", max_length=240)
    event_date = models.DateField("Event Date")
    event_location = models.CharField("Event Location", max_length=240, null=False) 
    event_price = models.IntegerField("Event Price", default=0)
    ticket_status = models.CharField("Ticket Status", max_length=10, choices=EVENT_STATUS_CHOICES, null=False) 
    ticket_start_time = models.TimeField("Ticket Start Time", null=False)   
    ticket_end_time = models.TimeField("Ticket End Time", null=False) 
    created = models.DateField("Created On", auto_now_add=True)

    def __str__(self):
        return self.event_name