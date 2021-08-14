from api.models import Message
from rest_framework import serializers, viewsets, permissions
from api.serializers import MessageSerializer
 
 
#Lead Viewset
class MessageViewSet(viewsets.ModelViewSet):
   queryset = Message.objects.all()
   permission_classes = [
       permissions.AllowAny
   ]
   serializer_class = MessageSerializer