from django.urls import path
from .views import homepage, Hompageview, Aboutpageview, Loginpageview

urlpatterns=[
    path('', Hompageview.as_view(), name='home'),
    path('about/', Aboutpageview.as_view(), name='about'),
    path('login/', Loginpageview.as_view(), name='login')
]