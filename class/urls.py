from django.urls import path


from . import views
from . import apiviews

urlpatterns = [
    # path('', views.auth),
    path('catalog/', views.catalog),
    # path('api/authorizations', apiviews.Autorizations.as_view()),
    # path('api/registrations', apiviews.Registraton.as_view()),
    # path('api/courses/<int:id>/list', apiviews.Сourses.as_view()),
    # path('api/courses/<int:id>/take', apiviews.TakeCourse.as_view()),
    # path('home/<int:id>/', views.auth)#Поменять
]

