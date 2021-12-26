from django.urls.conf import include, path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'', views.OrderViewset)

urlpatterns = [
    path('addproduct/<str:id>/<str:token>/', views.Addproduct, name='order.addproduct'),
    path('', include(router.urls))
]