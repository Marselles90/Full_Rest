from .serializers import UserSerializers
from rest_framework.viewsets import ModelViewSet
from .models import User

from .tasks import send_email_task, send_phone



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    
    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        phone = request.data.get('phone')
        user = super().create(request, *args, **kwargs)
        send_email_task.delay(email)
        send_phone.delay(phone)
        return user
       
       
       
