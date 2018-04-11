from django.conf.urls import url
from django.urls import path

from . import views
app_name = 'courses'
urlpatterns = [
    url(r"^$", views.AllPosts.as_view(), name="course_list"),
    
    url(
        r"by/(?P<username>[-\w]+)/$",
        views.UserPosts.as_view(),
        name="for_user"
    ),
    url(
        r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",
        views.SinglePost.as_view(),
        name="single"
    ),
    url(
        r"delete/(?P<pk>\d+)/$",
        views.DeletePost.as_view(),
        name="delete"
    ),
     path('<int:course_pk>/<int:step_pk>/', views.StepDetailView.as_view(),
     name='step'),
     path('create/', views.CreatePost.as_view(), name="create_course"),
     path('step-create/', views.CreateStep.as_view(), name="step_create"),
     path('edit-course/<int:pk>/', views.EditView.as_view(), name="edit_course"),
     path('edit-step/<int:pk>/', views.EditView.as_view(), name="edit_step"),
     path('delete-<int:step_pk>/edit-step/<int:pk>/', views.DeleteView.as_view(), name="delete_course"),

path('delete/<int:course_pk>/<int:step_pk>/', views.DeleteStepDetail.as_view(), name='delete_step_detail'),     path('<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
     path('my-courses/', views.MyView.as_view(), name="myview"),
     path('edit-step/<int:course_pk>/<int:step_pk>/', views.EditStepDetail.as_view(), name='edit_step_detail'),

]
