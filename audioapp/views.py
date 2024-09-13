from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import  HttpResponse
from django.views.generic import  ListView, FormView, DetailView
from rest_framework.views import APIView
from django.urls import  reverse_lazy
from .models import Track
from .forms import  TrackForm

# Create your views here.
@api_view()
def index(request):
    # return HttpResponse({'message': 'Hello World!'})
    return Response({'message': 'Hello World!'})


class TracksListView(ListView):
    model = Track

class AddTrackView(FormView):
    model = Track
    form_class = TrackForm
    template_name = 'audioapp/add_track.html'
    success_url = reverse_lazy("list")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class TrackView(DetailView):
    model = Track