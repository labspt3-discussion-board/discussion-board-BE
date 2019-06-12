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
    path('users/oauth/google/' ,views.UserOauthGoogle.as_view() ,name='Google oauth login'),
    path('users/oauth/facebook/' ,views.UserOauthFacebook.as_view() ,name='Facebook oauth login'),
    path('subtopics/'   ,views.SubtopicList.as_view() ,name='subtopic list'),
    path('subtopics/<id>/'   ,views.SubtopicDetails.as_view() ,name='subtopic details'),
    path('subtopics/<id>/discussions/'   ,views.SubtopicDiscussions.as_view() ,name='subtopic discussions'),
    path('discussions/'   ,views.DiscussionList.as_view() ,name='discussion list'),
    path('discussions/<id>/'   ,views.DiscussionDetails.as_view() ,name='discussion details'),
    path('discussions/<id>/comments/'   ,views.DiscussionComments.as_view() ,name='discussion comments'),
    path('topdiscussions/'   ,views.TopDiscussions.as_view() ,name='top ten discussions'),
    path('comments/'   ,views.CommentList.as_view() ,name='comments list'),
    path('comments/<id>/'   ,views.CommentDetails.as_view() ,name='comment details'),
]
