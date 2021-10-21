from django.urls.conf import include, path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'', views.UserViewsets)

urlpatterns = [
    path('login/', views.signin, name='signin'),
    path('logout/<int:id>/', views.signout, name='signout'),

    path('', include(router.urls))
]