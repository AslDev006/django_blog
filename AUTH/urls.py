from django.urls import path
from .views import *
urlpatterns = [
   path('signup/', SignupPageView, name='signup_page'),
    path('login/', LoginPageView, name='login_page'),
    path('logout/', LogoutPageView, name='logout_page'),
    path('signup/<id>/', Signup2PageView, name='signup2_page'),
    path(r'^password/$', change_password, name='change_password'),
    path('users/<id>/', ProfilePage, name='profile_page'),
]