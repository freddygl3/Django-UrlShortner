from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('create', views.Create.as_view(), name="create"),
    path('<str:pk>', views.UrlGo.as_view(), name="urlgo"),
]