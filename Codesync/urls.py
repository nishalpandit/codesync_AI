from django.urls import path
from django.urls import path
from . import views 
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('auth/', auth, name='auth'),
    path('billing/', billing, name='billing'),
    path('pulls/', pulls, name='pulls'),
    path('repo/', repo, name='repo'),
    path('setting/', settings, name='setting'),
    path('dashboard/', dashboard, name='dashboard'),
    path('docs/api/', api, name='api'),
    path('blog/', blog, name='blog'),
    path('careers/', career, name='carrer'),
    path('community/', community, name='community'),
    path('contact/', contact, name='contact'),
    path('features/', features, name='features'),
    path('change_pass/', change_pass, name='change_pass'),
    path('help/', help_center, name='help_center'),
    path('privacy/', policy, name='policy'),
    path('security/', security, name='security'),
    path('status/', system_status, name='status'),
    path('terms/', terms_condition, name='terms'),
    path('logout/', logouts, name='logout'),

    path('team/', views.team, name='team'),
    path('create_repo/', views.create_repo, name='create_repo'),
    path('load_repo/<int:id>/', views.load_repo, name='load_repo'),
    path('save_repo/<int:id>/', views.save_repo, name='save_repo'),
    path('delete_repo/<int:id>/', views.delete_repo, name='delete_repo'),


]


