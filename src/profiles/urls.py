from django.conf.urls import url


from .views import ProfileDetailSlugView, profileCreate

urlpatterns = [
    url(r'^$', profileCreate, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', ProfileDetailSlugView.as_view(), name='views'),
]

