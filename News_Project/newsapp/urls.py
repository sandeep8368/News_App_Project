from django.contrib import admin
from django.urls import path
from newsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/',views.news_view ),
    path('sports/',views.sports_view),
    path('business/',views.business_view),
    path('movie/',views.movie_view),
]
