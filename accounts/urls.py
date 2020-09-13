from django.urls import path

from .views import (
    Index,
    Home,
    SignUpView
)



urlpatterns = [

    # path('login/', Index.as_view(), name = 'login'),
    path('', Home.as_view(), name = 'home'),
    path('signup/',SignUpView.as_view(), name='sign_up')

]
