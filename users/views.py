from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm
from django.db.models import Q
from .utils import searchProfiles, paginateProfiles

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
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('events')
        
        else:
            messages.error(request, 'An error has occurred during registation!')

    context = {'page':page, 'form':form}
    return render(request, 'users/login-register.html', context)

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

# @login_required(login_url="login")
# def addSkill(request):
#     profile = request.user.profile
#     form = SkillForm()

#     if request.method == 'POST':
#         form = SkillForm(request.POST)
#         if form.is_valid():
#             skill = form.save(commit=False)
#             skill.owner = profile
#             skill.save()
#             return redirect('account')

#     context = {'form':form}
#     return render(request, 'users/add-skill.html', context)


# @login_required(login_url="login")
# def updateSkill(request, pk):
#     profile = request.user.profile
#     skill = profile.skill_set.get(id=pk)
#     form = SkillForm(instance=skill)

#     if request.method == 'POST':
#         form = SkillForm(request.POST, instance=skill)
#         if form.is_valid():
#             form.save()
#             return redirect('account')

#     context = {'form':form}
#     return render(request, 'users/update-skill.html', context)

# @login_required(login_url="login")
# def deleteSkill(request, pk):
#     skill = Skill.objects.get(id=pk)
#     if request.method == 'POST':
#         skill.delete()
#         return redirect('account')
#     context = {'skill':skill}
#     return render(request, 'users/delete-skill.html', context)