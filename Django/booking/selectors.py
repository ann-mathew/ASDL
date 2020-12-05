from .models import Ticket, Train, Station

def getAvailableTrains(source: str, destination: str, time, coach_class: str, seats: int):

    allTrains = Train.objects.all()
    avail_train = {}
    reserved_train = {}
    for train in allTrains:

        if train.route.filter(station_name=source).first():
            if train.route.filter(station_name=destination).first():
                if train.total_seats > seats:
                    #if time<train.arrival_time:   
                    avail_train[train.train_id] = {
                                "train_id": train.train_id,
                                "train_name": train.train_name,
                                "available_seats": train.remaining_seats,
                                "arrival": train.arrival_time,
                                "departure": train.departure_time
                    }
                else:
                    reserved_train[train.train_id] = {
                                "train_id": train.train_id,
                                "train_name": train.train_name,
                                "available_seats": -(train.remaining_seats - 1),
                                "arrival": train.arrival_time,
                                "departure": train.departure_time
                    }

            

    if not bool(avail_train) and not bool(reserved_train):  
        return None
    else:
        return { 'avail_train': avail_train, 'reserved_train': reserved_train }

