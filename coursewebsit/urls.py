from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404, handler500
from .views import SearchView
from .import views
from django.views.generic import View
from django.conf import settings
from django.views.static import serve
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    #url(r"^accounts/", include("accounts.urls", namespace="accounts")),
    #url(r"^accounts/", include("django.contrib.auth.urls")),

    url(r"^courses/", include("courses.urls")),

    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    
    path('search/', SearchView.as_view(), name='search'), 
    path('accounts/signup/', views.SignUpView.as_view(), name="signup"),
    url(r'^profile/(?P<username>\w+)/$', views.myprofileview, name="detail_profile")
]

handler404 = 'courses_views.error_404'
handler500 = 'courses_views.error_500'




if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]