from django.shortcuts import render

def blankPage(request):
    page = "blank"
    context = {'page':page}
    return render(request, 'events/blank.html',context)

def eventsPage(request):
    page = "events"
    context = {'page':page}
    return render(request, 'events/events.html',context)

def aboutPage(request):
    page = "about"
    context = {'page':page}
    return render(request, 'events/about.html', context)
