from django.conf.urls import url

from .views import my_profile,logout,register,login

app_name = 'accounts'

urlpatterns = [	
	url(r'^profile/$',my_profile, name='my_profile'),
	url(r'^logout/$',logout, name='logout'),
	url(r'^register/$',register, name='register'),
	url(r'^login/$',login, name='login')
]

