from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.generate,name='generate'),
    path('history/<str:psw>/',views.history,name='history'),

]
