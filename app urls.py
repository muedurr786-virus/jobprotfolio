from django.urls import path
from .views import *

urlpatterns = [
    path('register/', registerpage, name='register'),
    path('', loginpage, name='login'), 
    path('logout/', logoutpage, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/update/', updateprofilepage, name='update_profile'),
    path('consume/', consumeCaloryPage, name='consume_calory'),
]
