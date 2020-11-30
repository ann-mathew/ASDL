from .models import Ticket, Train, Station

def getAvailableTrains(source: str, destination: str, time, coach_class: str, seats: int):

    allTrains = Train.objects.all()
    avail_train = {}
    for train in allTrains:
        if train.total_seats > seats:
            if train.route.filter(station_name=source).first():
                if train.route.filter(station_name=destination).first():
                    #if time<train.arrival_time:   
                    avail_train[train.train_id] = {
                                "train_id": train.train_id,
                                "train_name": train.train_name,
                                "available_seats": train.total_seats,
                                "arrival": train.arrival_time,
                                "departure": train.departure_time
                    }
            
    print("avail_train")
    if not bool(avail_train):
        return None
    else:
        return avail_train

