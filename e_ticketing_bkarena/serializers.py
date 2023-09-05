from rest_framework import serializers
from .models import UserTbl, TicketTbl

class UserTblSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTbl 
        fields = ['pk', 'pin', 'full_name', 'email', 'created']


class TicketTblSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketTbl 
        fields = ['pk', 'user', 'event_name', 'event_date', 'event_location', 'event_price', 'ticket_status', 'ticket_start_time', 'ticket_end_time', 'created']