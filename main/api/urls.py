from rest_framework import routers
from .api import MessageViewSet
 
 
router = routers.DefaultRouter()
router.register('api/message', MessageViewSet, 'message')
 
 
urlpatterns = router.urls
