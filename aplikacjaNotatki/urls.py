from django.urls import path

from aplikacjaNotatki import views

app_name = 'aplikacjaNotatki'

urlpatterns = [
    path('', views.NotesView.as_view(), name='post_list'),
]