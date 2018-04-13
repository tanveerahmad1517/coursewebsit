from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from .views import SearchView
from .import views
from django.views.generic import View
from django.conf import settings
from django.views.static import serve
handler404 = 'djangosa.handle_404'

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    #url(r"^accounts/", include("accounts.urls", namespace="accounts")),
    #url(r"^accounts/", include("django.contrib.auth.urls")),

    url(r"^courses/", include("courses.urls")),
    path('', include('django.contrib.auth.urls')),
    path('search/', SearchView.as_view(), name='search'), 
    path('accounts/signup/', views.SignUpView.as_view(), name="signup"),
    url(r'^profile/(?P<username>\w+)/$', views.myprofileview, name="detail_profile")
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

    
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
