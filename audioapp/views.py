from django.core.exceptions import ValidationError
from django.db import IntegrityError

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import  HttpResponse
from django.views.generic import  ListView, FormView, DetailView,CreateView
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

class AddTrackView(CreateView):
    model = Track
    form_class = TrackForm
    template_name = 'audioapp/add_track.html'
    success_url = reverse_lazy("list")

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError:
            # Integrity error may occur when unique_together constraint is violated
            # author name and song title specifically
            return render(self.request,
                          self.template_name,
                          {'error': "Can't upload track. Perhaps track with such name by this author already exists?",
                           "form": form
                           })

class TrackView(DetailView):
    model = Track