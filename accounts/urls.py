from django.urls import path

from .views import (
    Index,
    home,
    SignUpView
)



urlpatterns = [

    # path('login/', Index.as_view(), name = 'login'),
    path('', home, name = 'home'),
    path('signup/',SignUpView.as_view(), name='sign_up')

]
