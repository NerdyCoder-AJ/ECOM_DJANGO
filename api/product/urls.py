from django.urls.conf import include, path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]