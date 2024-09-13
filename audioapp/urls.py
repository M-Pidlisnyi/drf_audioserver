from django.urls import path
from .views import index, TracksListView, AddTrackView,TrackView


#app/...
urlpatterns =[
    path('', index, name='index'),
    path('list/', TracksListView.as_view(), name='list'),
    path('add/', AddTrackView.as_view(), name='add'),
    path('track/<pk>', TrackView.as_view(), name='track')
]
