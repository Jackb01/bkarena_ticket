from django.urls import include, path
from .views import UserTblCreate, UserTblList, UserTblDetail, UserTblDelete, TicketTblCreate, TicketTblList, TicketTblDetail, TicketTblDelete


urlpatterns = [
    path('tickets/create/', TicketTblCreate.as_view(), name='create-ticket-tbl'),
    path('tickets/', TicketTblList.as_view()),
    path('tickets/<int:pk>/', TicketTblDetail.as_view(), name='retrieve-ticket-tbl'),
    path('tickets/delete/<int:pk>/', TicketTblDelete.as_view(), name='delete-ticket-tbl'),


    path('users/create/', UserTblCreate.as_view(), name='create-user-tbl'),
    path('users/', UserTblList.as_view()),
    path('users/<int:pk>/', UserTblDetail.as_view(), name='retrieve-user-tbl'),
    path('users/delete/<int:pk>/', UserTblDelete.as_view(), name='delete-user-tbl'),
]