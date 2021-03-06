from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^$', views.me, name="index"),
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^tf/(?P<source>[register|login]+)', views.two_factor_view, name='two-factor-verification'),
    # url(r'tf/submit/$', views.two_factor_view, name='tfv'),
]
