from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.register_user,name = 'registeruser'),
    path('loginuser/',views.login_user,name = 'loginuser'),
    path('main/',views.main,name = 'main'),
    path('logoutuser/',views.logout_user,name = 'logoutuser'),
]