from django.urls.conf import include, path
from . import views


urlpatterns = [
    path('gettoken/<str:id>/<str:token>/', views.genrate_token, name='token.genrate'),
    path('process_payment/<str:id>/<str:token>/', views.process_payment, name='process.payment'),
]