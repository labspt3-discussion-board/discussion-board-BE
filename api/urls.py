from django.urls import path
from .           import views

urlpatterns = [
    path(''                ,views.Index.as_view()       ,name='index'       ),
    # path('create-user/'    ,views.createUser          ,name='create-user' ),
    path('users/'          ,views.UserList.as_view()    ,name='users'       ),
    # path('users/<uuid>/'   ,views.UserDetails.as_view() ,name='user details'),
    path('users/login/'    ,views.UserLogin.as_view()   ,name='login'       ),
    path('users/logout/'   ,views.UserLogout.as_view()  ,name='logout'      ),
    path('users/login/check/' ,views.UserLoginCheck.as_view() ,name='login check'),
    path('subtopics/'   ,views.SubtopicList.as_view() ,name='subtopic list'),
    # path('subtopics/<uuid>/'   ,views.SubtopicDetails.as_view() ,name='subtopic details'),
    # path('discussions/'   ,views.DiscussionList.as_view() ,name='discussion list'),
    # path('discussions/<id>/'   ,views.DiscussionDetails.as_view() ,name='discussion details'),
    # path('comments/'   ,views.CommentList.as_view() ,name='comments list'),
    # path('comments/<id>/'   ,views.CommentDetails.as_view() ,name='comment details'),
]
