from django.urls import path, include
from .views import *

urlpatterns = [
    path('add_user', add_user, ),
    path('login_users', login_users, ),
    path('init_data',init_data,),
    path('test_data',test_data,),
    path('get_data',get_data,),
    path('sos_data',sos_data,),
    path('save_evaluate',save_evaluate,),
    path('get_evaluate',get_evaluate,),
    path('get_classify',get_classify,),
    path('other_page',other_page,),
]