
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_person', views.search_person, name='search_person'),
    path('add_a_person', views.add_a_person, name='add_a_person'),
    path('see_my_adds', views.see_my_adds, name='see_my_adds'),
    path('person_details/<id>', views.person_details, name='person_details'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('account', views.account, name='account'),
    path('login_func', views.login_func, name='login_func'),
    path('func_logout', views.func_logout, name='func_logout'),
    path('email/confirmation/<str:activation_key>/', views.email_confirm, name='email_activation'  ),
]
