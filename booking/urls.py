from django.urls import path

from .views import (BookTicketView, CancelSingleTicketView, GetAvailableTrains,
                    GetTicketView, GetTrainView, LockSeatsView,
                    TransactionDetailsView, CancelTicketByTransactionView)

urlpatterns = [
    path('availtrains/', GetAvailableTrains.as_view()),
    path('bookticket/', BookTicketView.as_view()),
    path('getticket/<str:ticket_id>', GetTicketView.as_view()),
    path('gettrain/<str:train_id>', GetTrainView.as_view()),
    path('cancel_ticket/', CancelSingleTicketView.as_view()),
    path('cancel_ticket_by_transaction/', CancelTicketByTransactionView.as_view()),
    path('get_transaction_tickets/', TransactionDetailsView.as_view()),
    path('lock/', LockSeatsView.as_view()),
    
]
