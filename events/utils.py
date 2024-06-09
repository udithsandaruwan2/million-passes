from .models import Event
from django.db.models import Q
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchEvents(request):
    search_query = '' 
    if request.GET.get('search'):
        search_query = request.GET.get('search', '')
    
    events = Event.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) 
        # Q(owner__name__icontains=search_query) 
    )
    
    return events, search_query