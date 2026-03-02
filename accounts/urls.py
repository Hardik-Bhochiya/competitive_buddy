from django.urls import path
from .views import home, signup_view, login_view, logout_view, profile_view

urlpatterns = [
    path('', home, name="home"),
    path('signup/', signup_view, name="signup"),   # ← THIS LINE MUST EXIST
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('profile/', profile_view, name="profile"),
]