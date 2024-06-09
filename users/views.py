from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.db.models import Q
from .utils import searchEvents



def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exists!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'User login successfully!')
            if 'ADMIN' in username:
                return redirect('admin')
            else:
                return redirect('events')
            
        else:
            messages.error(request, 'Username or password is incorrect!')
    
    context = {'page':page}

    return render(request, 'users/login-register.html', context)

@login_required(login_url="login")
def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('events')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            if 'ADMIN' in user.username:
                return redirect('admin')
            else:
                return redirect('events')
        
        else:
            messages.error(request, 'An error has occurred during registation!')

    context = {'page':page, 'form':form}
    return render(request, 'users/login-register.html', context)

@login_required(login_url="login")
def adminPanel (request):
    page = 'dashboard'
    search_query = ''
    profile = request.user.profile
    events = profile.event_set.filter(owner=profile)

    if request.GET.get('search'):
        events, search_query = searchEvents(request, profile)

    context = {'page':page, 'profile':profile, 'events':events, 'search_query':search_query}
    return render(request, 'users/admin-panel.html', context)



# @login_required(login_url="login")
# def profiles(request):
#     profiles, search_query = searchProfiles(request)
#     custom_range, profiles = paginateProfiles(request, profiles, 9)
#     context = {'profiles': profiles, 'search_query':search_query, 'custom_range':custom_range}
#     return render(request, 'users/profiles.html', context)


# @login_required(login_url="login")
# def userProfile(request, pk):
#     profile = Profile.objects.get(id=pk)

#     context = {'profile':profile}
#     return render(request, 'users/user-profile.html', context)

# @login_required(login_url="login")
# def userAnalytics(request):
#     profile = request.user.profile
    
#     context = {'profile':profile}
#     return render(request, 'users/analytics.html', context)

# @login_required(login_url="login")
# def userAccount(request):
#     profile = request.user.profile

#     topskills = profile.skill_set.exclude(description__exact="")
#     otherskills = profile.skill_set.filter(description="")
        
#     context = {'profile': profile, 'topskills': topskills, 'otherskills': otherskills}
#     return render(request, 'users/account.html', context)

# @login_required(login_url="login")
# def updateProfile(request):
#     profile = request.user.profile
#     form = ProfileForm(instance=profile)

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('account')

#     context = {'form':form}
#     return render(request, 'users/update-profile.html', context)
