from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about_us, name='about'),
    path('auth/', auth, name='auth'),
    path('billing/', billing, name='billing'),
    path('pulls/', pulls, name='pulls'),
    path('repo/', repo, name='repo'),
    path('setting/', settings, name='setting'),
    path('dashboard/', dashboard, name='dashboard'),
    path('docs/api/', api_docs, name='api'),
    path('blog/', blog, name='blog'),
    path('careers/', career, name='carrer'),
    path('community/', community, name='community'),
    path('contact/', contact_us, name='contact'),
    path('features/', features, name='features'),
    path('change_pass/', change_pass, name='change_pass'),
    path('help/', help_center, name='help_center'),
    path('privacy/', privacy_policy, name='policy'),
    path('security/', security, name='security'),
    path('status/', system_status, name='status'),
    path('terms/', terms_condition, name='terms'),
    path('signup/', signup_form, name='signup'),
    path('logout/', logouts, name='logout'),
    path( 'notepad/', notepad, name='notepad' ),
]


