
from django.db.models import Q
from events.models import Event
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchEvents(request, profile):
    search_query = '' 
    if request.GET.get('search'):
        search_query = request.GET.get('search', '')


        events = Event.objects.distinct().filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query),
            owner=profile
        )

    
    return events, search_query
















# from .models import Profile
# from django.db.models import Q
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# def searchProfiles(request):
#     search_query = '' 
#     if request.GET.get('search'):
#         search_query = request.GET.get('search', '')
        
#     profiles = Profile.objects.filter(
#         Q(name__icontains=search_query) | 
#         Q(short_intro__icontains=search_query)
#         )
    
#     return profiles, search_query

# def paginateProfiles(request, profiles, results):
#     page = request.GET.get('page')
#     paginator = Paginator(profiles, results)
    
#     try:
#         profiles = paginator.page(page)
#     except PageNotAnInteger:
#         page = 1
#         profiles = paginator.page(page)
#     except EmptyPage:
#         page = paginator.num_pages
#         profiles = paginator.page(page)
        
#     left_index = (int(page) - 1)
    
#     if left_index < 1:
#         left_index = 1
        
#     right_index = (int(page) + 2)
    
#     if right_index > paginator.num_pages:
#         right_index = paginator.num_pages+1
    
#     custom_range = range(left_index, right_index)
#     return custom_range, profiles