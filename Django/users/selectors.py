from booking.models import Ticket
from datetime import datetime
import pytz
from django.utils import timezone

def getBookings(user: str):

    allBookings = Ticket.objects.filter(user=user)

    bookings = {}

    for booking in allBookings:
        bookings[booking.ticket_id] = {
                        "ticket_number": booking.ticket_number, 
                        "passenger": booking.passenger.name,
                        "train": booking.train.train_name,
                        "seat_no": booking.seat_no,
                        "book_date": booking.book_date,
                        "price": booking.price,
                        "boarding": booking.boarding.station_name,
                        "destination": booking.destination.station_name            
                                }                    
                      
            

    if not bool(bookings):
        return None
    else:
        return { 'bookings': bookings }


