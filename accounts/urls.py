from django.urls import path
from . import views
from accounts.views import LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.indexView,name="index"),
    path('register/',views.registerView,name="register"),
    path('login/',LoginView.as_view(),name="login"),
    path('detail/',views.UserDetailView,name="detail"),
    path('detail/edit/<int:id>', views.Update_view,name='update'),
    path('detail/delete/<int:id>', views.Delete_view,name='delete'),
    path('logout/',LogoutView.as_view(),name="logout"),
]
