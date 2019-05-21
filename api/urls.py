from django.urls import path
from .           import views

urlpatterns = [
    path(''                ,views.Index.as_view()       ,name='index'       ),
    # path('create-user/'    ,views.createUser          ,name='create-user' ),
    path('users/'          ,views.UserList.as_view()    ,name='users'       ),
    path('users/<uuid>/'   ,views.UserDetails.as_view() ,name='user details'),
]