from django.shortcuts import render
from .models import UserTbl, TicketTbl
from rest_framework import generics
from .serializers import UserTblSerializer, TicketTblSerializer

#-------------------- Interface Here ----------------------#

####------------  User Views --------------####

class UserTblCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new User
    queryset = UserTbl.objects.all(),
    serializer_class = UserTblSerializer

class UserTblList(generics.ListAPIView):
    # API endpoint that allows all users to be viewed.
    queryset = UserTbl.objects.all()
    serializer_class = UserTblSerializer

class UserTblDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single User by pk.
    queryset = UserTbl.objects.all()
    serializer_class = UserTblSerializer

class UserTblDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a user record to be deleted.
    queryset = UserTbl.objects.all()
    serializer_class = UserTblSerializer






####------------  Ticket Views --------------####

class TicketTblCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new ticket
    queryset = TicketTbl.objects.all(),
    serializer_class = TicketTblSerializer

class TicketTblList(generics.ListAPIView):
    # API endpoint that allows all tickets to be viewed.
    queryset = TicketTbl.objects.all()
    serializer_class = TicketTblSerializer

class TicketTblDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Ticket by pk.
    queryset = TicketTbl.objects.all()
    serializer_class = TicketTblSerializer

class TicketTblDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a ticket record to be deleted.
    queryset = TicketTbl.objects.all()
    serializer_class = TicketTblSerializer