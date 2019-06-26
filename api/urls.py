from django.urls import path
from .           import views

urlpatterns = [
    path(''                      ,views.Index.as_view()       ,name='index'       ),
    # path('create-user/'        ,views.createUser          ,name='create-user'   ),
    path('users/'                ,views.UserList.as_view()    ,name='users'       ),
    path('users/<id>/'       ,views.UserDetails.as_view() ,name='user details'),
    path('users/login/'          ,views.UserLogin.as_view()   ,name='login'       ),
    path('users/register/'       ,views.UserRegister.as_view()   ,name='register' ),
    path('users/logout/'         ,views.UserLogout.as_view()  ,name='logout'      ),
    path('users/login/check/'    ,views.UserLoginCheck.as_view() ,name='login check'),
    path('users/oauth/google/'   ,views.UserOauthGoogle.as_view() ,name='Google oauth login'),
    path('users/oauth/facebook/' ,views.UserOauthFacebook.as_view() ,name='Facebook oauth login'),
    path('subforums/'            ,views.SubforumList.as_view() ,name='Subforum list'),
    path('subforums/<id>/'       ,views.SubforumDetails.as_view() ,name='Subforum details'),
    path('subforums/<id>/discussions/'   ,views.SubforumDiscussions.as_view() ,name='subforum discussions'),
    path('subforums/<id>/members/'   ,views.SubforumMembers.as_view() ,name='subforum members'),
    path('discussions/'   ,views.DiscussionList.as_view() ,name='discussion list'),
    path('discussions/<id>/'   ,views.DiscussionDetails.as_view() ,name='discussion details'),
    path('discussions/<id>/vote/'   ,views.DiscussionVote.as_view() ,name='discussion vote'),
    path('discussions/<id>/comments/'   ,views.DiscussionComments.as_view() ,name='discussion comments'),
    path('topdiscussions/'   ,views.TopDiscussions.as_view() ,name='top ten discussions'),
    path('comments/'   ,views.CommentList.as_view() ,name='comments list'),
    path('comments/<id>/'   ,views.CommentDetails.as_view() ,name='comment details'),
    path('usertosubforum/'   ,views.UserToSubforumList.as_view() ,name='User to Subforum List'),
    path('usertosubforum/<id>/'   ,views.UserToSubforumDetails.as_view() ,name='User to Subforum Details'),
]
