from django.urls import path

from analysis import views

urlpatterns = [

    path('', views.login, name = "login"),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path(
        "charts/",
        views.charts,
        name='charts'
    )
    

]
