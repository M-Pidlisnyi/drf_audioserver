from django.urls import path
from .views import index, TracksListView, AddTrackView


#app/...
urlpatterns =[
    path('', index, name='index'),
    path('list/', TracksListView.as_view(), name='list'),
    path('add/', AddTrackView.as_view(), name='add')
]
