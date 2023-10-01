from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, UserUpdateView, generate_new_password

''' LogoutView, RegisterView, UserUpdateView, set_new_password, \
    UserConfirmEmailView, \
    UserConfirmedView, password_reset, UserConfirmationSentView, UserListView, UserUpdateManagerView
    '''

app_name = UsersConfig.name


urlpatterns = [

    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", UserUpdateView.as_view(), name="profile"),
    path("profile/gen_password", generate_new_password, name="gen_password"),
]

'''path("logout/", LogoutView.as_view(), name="logout"),
    
    path('email_confirmation_sent/', UserConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('confirm_email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email_confirmed/', UserConfirmedView.as_view(), name='email_confirmed'),
    path("profile/", UserUpdateView.as_view(), name="profile"),
    path("profile/set_password", set_new_password, name="set_password"),
    path('password_reset/', password_reset, name='password_reset'),
    path('users_list/', UserListView.as_view(), name='users_list'),
    path('edit_user/<int:pk>/', UserUpdateManagerView.as_view(), name='edit_user'),'''