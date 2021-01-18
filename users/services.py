from .models import User
from .selectors import getUserIDFromToken

def setUserData(data):
    token = data.pop('token', None)
    if token:
        user = getUserIDFromToken(token)
        user = User.objects.get(username=user)
        user.full_name = data['full_name'] or user.full_name
        user.email = data['email'] or user.email
        user.phoneNo = data['phoneNo'] or user.phoneNo
        user.age = data['age'] or user.age
        user.save()
        return True
    else:
        return False


def deleteUser(token):
    user = getUserIDFromToken(token)
    user = User.objects.get(username=user)
    user.delete()
    return True
