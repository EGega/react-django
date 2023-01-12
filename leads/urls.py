from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('leads', LeadViewSet, 'leads') # the leads here is just a name

urlpatterns = [

]
urlpatterns += router.urls